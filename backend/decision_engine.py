def evaluate_student(profile, major):

    score = {
        "专业基础": 70,
        "编程能力": 50,
        "实践能力": 30,
        "职业准备": 40
    }


    total = (
        score["专业基础"] * 0.3
        +
        score["编程能力"] * 0.3
        +
        score["实践能力"] * 0.2
        +
        score["职业准备"] * 0.2
    )


    return {
        "scores": score,
        "total_score": int(total)
    }