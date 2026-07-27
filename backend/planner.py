from prompt_builder import build_prompt
from deepseek_api import ask_deepseek


def generate_answer(
        question,
        profile,
        evaluation,
        major,
        school
):

    # 生成AI专用Prompt
    prompt = build_prompt(
        question,
        profile,
        evaluation,
        major,
        school
    )


    # 调用大模型
    answer = ask_deepseek(
        prompt
    )


    return answer