# modules/prompt_builder.py

def build_prompt(goal, years, resume_text, appeal_axis, realism="realistic"):
    """
    ユーザー入力に基づいて、未来の職務経歴書を生成するプロンプトを作成する。
    realism: "realistic"（現実寄り）または "ambitious"（高い目標）
    """

    realism_instruction = {
        "realistic": "実現可能な範囲での成長にとどめてください。",
        "ambitious": "未来の実績には大胆な飛躍や挑戦的な成長を含めて構いません。"
    }

    tone = realism_instruction.get(realism, realism_instruction["realistic"])

    prompt = f"""
あなたは優秀なキャリアアドバイザーです。
以下の職務経歴書をもとに、{years}年後に「{goal}」という目標を達成した人物の職務経歴書（未来バージョン）を作成してください。

【重視すべきアピール軸】「{appeal_axis}」を強く印象づける構成にしてください  
【実績レベル】{tone}  
【文章トーン】前向きで自然な日本語、読みやすく説得力のある表現にしてください  
【出力形式】Markdown形式で以下の構成で記述してください：

---
- 職務要約（未来の実績を含む）
- 保有スキル・経験（未来のスキルも含めてOK）
- 具体的なプロジェクト例（未来のものを2～3件）
- 今後のキャリア展望（任意で可）
---

【現在の職務経歴書】
{resume_text}
""".strip()

    return prompt
