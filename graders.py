from models import Reward

def normalize_reward(score: float) -> float:
    if score <= 0:
        return 0.01
    elif score >= 1:
        return 0.99
    return float(score)

def grade_easy(result):
    if result["action"] == "accept":
        return Reward(score=normalize_reward(0.99), feedback="Accepted optimal offer")
    return Reward(score=normalize_reward(0.01), feedback="Should accept high offer")


def grade_medium(result):
    if result["action"] == "counter":
        return Reward(score=normalize_reward(0.99), feedback="Good negotiation")
    elif result["action"] == "accept":
        return Reward(score=normalize_reward(0.5), feedback="Acceptable but not optimal")
    return Reward(score=normalize_reward(0.01), feedback="Poor decision")


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

    score = max(0, min(score, 1))
    score = normalize_reward(score)

    return Reward(
        score=score,
        feedback="Strategic evaluation"
    )
    
