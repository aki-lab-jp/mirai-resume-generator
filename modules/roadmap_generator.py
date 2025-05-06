# modules/roadmap_generator.py

def generate_roadmap(goal: str, years: int, appeal_axis: str) -> str:
    # 仮のテキストを返します（後でLLM連携予定）
    return f"""
    {years}年後に「{goal}」になるためのロードマップ：
    
    - ステップ1：必要なスキルを明確化し、学習計画を立てる
    - ステップ2：{appeal_axis}を活かせる社内プロジェクトに参画
    - ステップ3：実績を蓄積し、自走できる状態を目指す
    - ステップ4：社内外での影響力を広げ、専門家としての信頼を築く
    - ステップ5：目標達成し、次のステージを見据える
    """
