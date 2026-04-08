from fastapi import FastAPI
from env import MarketEnv
from tasks import ALL_TASKS
from models import Action

app = FastAPI()

env = None

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/reset")
def reset():
    global env
    env = MarketEnv(ALL_TASKS[0])
    obs = env.reset()

    return {
        "observation": {
            "buyer_offer": obs.buyer_offer,
            "listed_price": obs.listed_price,
            "round": obs.round,
            "max_rounds": obs.max_rounds
        },
        "info": {}
    }

@app.post("/step")
def step(action: dict):
    global env

    # Handle empty input safely
    action_type = action.get("action_type", "accept")

    act = Action(action_type=action_type)

    obs, reward, done, info = env.step(act)

    return {
        "observation": {
            "buyer_offer": obs.buyer_offer,
            "listed_price": obs.listed_price,
            "round": obs.round,
            "max_rounds": obs.max_rounds
        },
        "reward": {
            "score": reward.score,
            "feedback": reward.feedback
        },
        "done": done,
        "info": info if info else {}
    }