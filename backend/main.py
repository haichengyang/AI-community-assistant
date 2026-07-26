from knowledge import load_major,load_school
from planner import generate_answer


major = load_major()
school = load_school()


print("AI校园规划助手")

question = input("请输入问题：")


answer = generate_answer(question, major,school)


print("\n建议：")

for item in answer:

    print("-", item)