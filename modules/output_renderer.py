import streamlit as st

def render_result(result: str):
    st.subheader("あなたの未来職務経歴書（案）")
    st.markdown(result)

    if st.button("PDFとして保存"):
        st.info("※ PDF生成機能は今後実装予定です")
