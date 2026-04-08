from models import Reward

def grade_easy(result):
    if result["action"] == "accept":
        return Reward(score=1.0, feedback="Accepted optimal offer")
    return Reward(score=0.0, feedback="Should accept high offer")


def grade_medium(result):
    if result["action"] == "counter":
        return Reward(score=1.0, feedback="Good negotiation")
    elif result["action"] == "accept":
        return Reward(score=0.5, feedback="Acceptable but not optimal")
    return Reward(score=0.0, feedback="Poor decision")


def grade_hard(result):
    score = 0

    # 🔥 Profit-based reward
    profit_ratio = result["buyer_offer"] / result["listed_price"]

    if result["action"] == "accept":
        score += profit_ratio

    # 🔥 Reward negotiation
    if result["action"] == "counter":
        score += 0.3

    # 🔥 Urgency penalty (time pressure)
    score -= 0.15 * result["round"]

    # 🔥 Walk-away penalty
    if result["action"] == "reject" and result["round"] == 1:
        score -= 0.3

    return Reward(
        score=max(0, min(score, 1)),
        feedback="Strategic evaluation"
    )