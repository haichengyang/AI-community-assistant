from knowledge import load_major, load_school
from profile import StudentProfile
from decision_engine import evaluate_student
from planner import generate_answer
from report import generate_report


# =========================
# 1. 加载高校知识库
# =========================

major = load_major()

school = load_school()


# =========================
# 2. 创建学生画像
# =========================

student = StudentProfile(
    name="张三",
    school="河池学院",
    major="数据科学与大数据技术",
    grade="大一",
    goal="人工智能方向",
    skills=[
        "Python基础"
    ]
)


profile = student.get_profile()


# =========================
# 3. 学生成长能力评估
# =========================

evaluation = evaluate_student(
    profile,
    major
)


# =========================
# 4. 学生问题
# =========================

question = """
我是大一学生，
不知道未来应该怎么规划。
"""


# =========================
# 5. AI生成成长决策
# =========================

answer = generate_answer(
    question,
    profile,
    evaluation,
    major,
    school
)


# =========================
# 6. 生成成长报告
# =========================

report = generate_report(
    profile,
    evaluation,
    answer
)


# =========================
# 7. 输出结果
# =========================

print(report)