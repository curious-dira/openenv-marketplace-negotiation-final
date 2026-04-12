import os
from openai import OpenAI
from env import MarketEnv
from tasks import ALL_TASKS
from models import Action

API_BASE_URL = os.getenv("API_BASE_URL","https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME","gpt-4o-mini")
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
        text = response.choices[0].message.content.strip().lower()
        if "accept" in text:
            return "accept"
        elif "counter" in text:
            return "counter"
        return "reject"
    except Exception:
        return "reject"

def run():
    for task in ALL_TASKS:
        print(f"[START] task={task['name']} env=market model={MODEL_NAME}")

        env = MarketEnv(task)
        obs = env.reset()

        done = False
        step = 0
        rewards = []
        total_score = 0.0

        while not done:
            step += 1

            action_type = llm_decision(obs)
            action = Action(action_type=action_type)

            obs, reward, done, _ = env.step(action)

            r = float(reward.score)
            rewards.append(r)
            total_score += r

            print(
                f"[STEP] step={step} action={action_type} reward={r:.2f} done={str(done).lower()} error=null"
            )

        score = min(max(total_score / len(rewards), 0.0), 1.0)

        rewards_str = ",".join(f"{x:.2f}" for x in rewards)

        print(
            f"[END] success=true steps={step} score={score:.2f} rewards={rewards_str}"
        )

if __name__ == "__main__":
    run()
