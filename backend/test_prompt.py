print("测试开始")
from knowledge import load_major, load_school
from prompt_builder import build_prompt


major = load_major()

school = load_school()


prompt = build_prompt(
    "我是大一学生，不知道未来怎么办",
    major,
    school
)


print(prompt)