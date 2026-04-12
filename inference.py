import os
from openai import OpenAI
from env import MarketEnv
from tasks import ALL_TASKS
from models import Action

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN,
)

def llm_decision(obs):
    prompt = f"""
You are a marketplace seller.

Listed price: {obs.listed_price}
Buyer offer: {obs.buyer_offer}
Round: {obs.round}/{obs.max_rounds}

Choose one action:
- accept
- reject
- counter

Respond with ONLY one word: accept, reject, or counter.
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5,
        )

        action_text = response.choices[0].message.content.strip().lower()

        if "accept" in action_text:
            return "accept"
        elif "counter" in action_text:
            return "counter"
        else:
            return "reject"

    except Exception:
        if obs.buyer_offer > 0.9 * obs.listed_price:
            return "accept"
        elif obs.buyer_offer > 0.5 * obs.listed_price:
            return "counter"
        else:
            return "reject"

def run():
    for task in ALL_TASKS:
        print(f"[START] task={task['name']}")

        env = MarketEnv(task)
        obs = env.reset()

        done = False
        total_reward = 0.0

        while not done:
            action_type = llm_decision(obs)
            action = Action(action_type=action_type)

            obs, reward, done, _ = env.step(action)

            total_reward += reward.score

            print(f"[STEP] round={obs.round} action={action_type} reward={reward.score}")

        print(f"[END] task={task['name']} total_reward={total_reward}")

if __name__ == "__main__":
    run()
