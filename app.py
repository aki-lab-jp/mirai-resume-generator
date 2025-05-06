import streamlit as st
from modules import user_input, prompt_builder
from modules import llm_executor

# ステップ形式フォームの表示（STEP1〜STEP3）
user_input.step_form()

# STEP4：プロンプトを生成して表示
if st.session_state.get("step") == 4:
    prompt = prompt_builder.build_prompt(
        goal=st.session_state.goal,
        years=st.session_state.years,
        resume_text=st.session_state.resume_text,
        appeal_axis=st.session_state.appeal_axis,
        realism="realistic"  # ← 将来的に切替できるようにUI追加してもOK
    )

    st.subheader("生成されたプロンプト")
    st.code(prompt, language="markdown")

    if st.button("職務経歴書（未来版）を生成する"):
            with st.spinner("生成中です..."):
                result = llm_executor.generate_future_resume(prompt)
                st.session_state.generated_resume = result
                st.success("生成が完了しました！")

if st.session_state.get("generated_resume"):
    st.subheader("生成結果")
    st.markdown(st.session_state.generated_resume)