from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()


client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


def ask_deepseek(prompt):

    response = client.chat.completions.create(
        model="deepseek-chat",

        messages=[
            {
                "role": "system",
                "content": "你是一名专业的大学生涯规划助手"
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content