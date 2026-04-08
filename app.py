from fastapi import FastAPI
from env import MarketEnv
from tasks import ALL_TASKS
from models import Action

app = FastAPI()

env = None

@app.post("/reset")
def reset():
    global env
    env = MarketEnv(ALL_TASKS[0])
    obs = env.reset()
    return obs.dict()

@app.post("/step")
def step(action: dict):
    global env
    act = Action(**action)
    obs, reward, done, _ = env.step(act)
    return {
        "observation": obs.dict(),
        "reward": reward.dict(),
        "done": done
    }