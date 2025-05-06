# modules/llm_executor.py

import os
import openai
import streamlit as st
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# Azure OpenAI の設定
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

# APIクライアント初期化
openai.api_type = "azure"
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_version = AZURE_OPENAI_API_VERSION
openai.api_key = AZURE_OPENAI_API_KEY


def generate_future_resume(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            engine=AZURE_OPENAI_DEPLOYMENT,
            messages=[
                {"role": "system", "content": "あなたはプロのキャリアアドバイザーです。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )

        message = response["choices"][0]["message"]["content"]
        return message

    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
        return ""
