from pydantic import BaseModel

class Observation(BaseModel):
    buyer_offer: float
    listed_price: float
    round: int
    max_rounds: int


class Action(BaseModel):
    action_type: str  # "accept", "reject", "counter"


class Reward(BaseModel):
    score: float
    feedback: str = ""

    def _init_(self, **data):
        score = data.get("score", 0.5)

        if score <= 0:
            data["score"] = 0.01
        elif score >= 1:
            data["score"] = 0.99
        else:
            data["score"] = float(score)

        super()._init_(**data)

#final_fix