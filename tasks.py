from graders import grade_easy, grade_medium, grade_hard

task_easy = {
    "name": "high_offer",
    "data": {
        "listed_price": 1000,
        "buyer_offer": 950,
        "max_rounds": 1
    },
    "grader": grade_easy
}

task_medium = {
    "name": "medium_offer",
    "data": {
        "listed_price": 1000,
        "buyer_offer": 600,
        "max_rounds": 2
    },
    "grader": grade_medium
}

task_hard = {
    "name": "dynamic_negotiation",
    "data": {
        "listed_price": 1000,
        "buyer_offer": 300,
        "max_rounds": 3
    },
    "grader": grade_hard
}

ALL_TASKS = [task_easy, task_medium, task_hard]