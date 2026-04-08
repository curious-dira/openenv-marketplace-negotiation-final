from pydantic import BaseModel

class Observation(BaseModel):
    listed_price: float
    buyer_offer: float
    round: int
    max_rounds: int

class Action(BaseModel):
    action_type: str  # accept / reject / counter
    counter_price: float = 0

class Reward(BaseModel):
    score: float
    feedback: str