from knowledge import load_major, load_school
from prompt_builder import build_prompt
from deepseek_api import ask_deepseek


major = load_major()

school = load_school()


prompt = build_prompt(
    "我是河池学院数据科学专业大一学生，不知道未来怎么办",
    major,
    school
)


answer = ask_deepseek(prompt)


print(answer)