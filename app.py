import streamlit as st
from modules import user_input, prompt_builder, llm_executor

# フォーム（STEP 1～STEP 3）
user_input.step_form()

# STEP 4：プロンプト生成と職務経歴書の生成
if st.session_state.get("step") == 4:
    st.header("STEP 4：未来の職務経歴書を生成")

    prompt = prompt_builder.build_prompt(
        goal=st.session_state.goal,
        years=st.session_state.years,
        resume_text=st.session_state.resume_text,
        appeal_axis=st.session_state.appeal_axis,
        realism="realistic"
    )

    # 任意でプロンプト表示
    if st.checkbox("生成されたプロンプトを表示する", value=False):
        st.code(prompt, language="markdown")

    if st.button("職務経歴書（未来版）を生成する"):
        with st.spinner("生成中です..."):
            result = llm_executor.generate_future_resume(prompt)
            if result:
                st.session_state.generated_resume = result
                st.success("生成が完了しました！")

# 結果表示
if st.session_state.get("generated_resume"):
    st.subheader("🌟 未来の職務経歴書（現実寄りVer）")
    st.markdown(st.session_state.generated_resume)
