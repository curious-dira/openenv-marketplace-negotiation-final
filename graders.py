from models import Reward

def safe_score(score):
    return max(0.01, min(0.99, float(score)))

def grade_easy(result):
    if result["action"] == "accept":
        score = 0.95
    else:
        score = 0.05
    return Reward(score=safe_score(score), feedback="easy")

def grade_medium(result):
    if result["action"] == "counter":
        score = 0.9
    elif result["action"] == "accept":
        score = 0.6
    else:
        score = 0.05
    return Reward(score=safe_score(score), feedback="medium")

def grade_hard(result):
    score = 0.4

    if result["action"] == "accept":
        score += result["buyer_offer"] / result["listed_price"]

    if result["action"] == "counter":
        score += 0.2

    score -= 0.1 * result["round"]

    return Reward(score=safe_score(score), feedback="hard")
