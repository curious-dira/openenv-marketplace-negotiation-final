import random
from models import Observation, Action, Reward

class MarketEnv:
    def __init__(self, task):
        self.task = task

    def reset(self):
        self.state_data = self.task["data"].copy()
        self.round = 1

        # 🔥 Buyer personality (NEW)
        self.buyer_type = random.choice(["aggressive", "normal", "generous"])

        return Observation(
            listed_price=self.state_data["listed_price"],
            buyer_offer=self.state_data["buyer_offer"],
            round=self.round,
            max_rounds=self.state_data["max_rounds"]
        )

    def step(self, action: Action):

        # 🔥 Dynamic buyer response
        if action.action_type == "counter":
            if self.buyer_type == "aggressive":
                self.state_data["buyer_offer"] += 50
            elif self.buyer_type == "normal":
                self.state_data["buyer_offer"] += 100
            else:
                self.state_data["buyer_offer"] += 150

        result = {
            "listed_price": self.state_data["listed_price"],
            "buyer_offer": self.state_data["buyer_offer"],
            "action": action.action_type,
            "round": self.round
        }

        reward = self.task["grader"](result)

        # 🔚 Termination conditions
        done = (
            action.action_type in ["accept", "reject"]
            or self.round >= self.state_data["max_rounds"]
        )

        self.round += 1

        obs = Observation(
            listed_price=self.state_data["listed_price"],
            buyer_offer=self.state_data["buyer_offer"],
            round=self.round,
            max_rounds=self.state_data["max_rounds"]
        )

        return obs, reward, done, {}

    def state(self):
        return self.state_data
    
    #final_fix