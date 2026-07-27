def generate_report(profile, evaluation, answer):

    report = f"""
# 🎓 智育导航·大学生成长规划报告


## 一、学生画像

{profile}



## 二、成长能力评估

{evaluation}



## 三、AI成长规划建议

{answer}



---
本报告由智育导航智能决策系统生成。
"""

    return report