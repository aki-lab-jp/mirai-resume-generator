import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

endpoint = "https://gene-ai.openai.azure.com/"
model_name = "gpt-4o-mini"
deployment = "gpt-4o-mini"

subscription_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

def generate_future_resume(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "あなたは優秀なキャリアアドバイザーです。",
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_tokens=4096,
            temperature=1.0,
            top_p=1.0,
            model=deployment
        )

        result = response.choices[0].message.content.strip()
        return result
    
    except Exception as e:
        return f"⚠️ エラーが発生しました：{e}"

