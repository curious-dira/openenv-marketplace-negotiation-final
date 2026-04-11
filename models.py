from pydantic import BaseModel

class Reward(BaseModel):
    score: float
    feedback: str = ""

    def _init_(self, **data):
        score = data.get("score", 0.5)

        # 🔥 FORCE score into (0, 1)
        if score <= 0:
            data["score"] = 0.01
        elif score >= 1:
            data["score"] = 0.99
        else:
            data["score"] = float(score)

        super()._init_(**data)