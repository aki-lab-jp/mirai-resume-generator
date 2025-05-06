def build_prompt(goal, years, resume_text, appeal_axis, realism="realistic"):
    """
    各入力項目からプロンプトを生成する。
    realism: "realistic" or "ambitious"
    """
    
    base_instruction = f"""
あなたは優秀なキャリアアドバイザーです。
以下の職務経歴書を参考に、{years}年後に「{goal}」として活躍している未来の職務経歴書を作成してください。

アピールしたい軸は「{appeal_axis}」です。
"""

    # 実績のリアリティレベルを切り替え
    if realism == "ambitious":
        tone = "未来の実績には大胆な成長を含めて構いません。"
    else:
        tone = "実現可能な範囲での成長にとどめてください。"

    resume_section = f"\n---\n現在の職務経歴：\n{resume_text}\n---"

    return base_instruction + tone + resume_section
