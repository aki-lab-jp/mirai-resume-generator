import streamlit as st

def step_form():
    if "step" not in st.session_state:
        st.session_state.step = 1

    st.title("わたしの職務経歴書（未来版）")

    # STEP 1
    if st.session_state.step == 1:
        st.header("STEP 1：目指す姿を入力してください")
        st.session_state.goal = st.text_input("目指す姿（例：生成AIの専門家として社内外で活躍）")
        st.session_state.years = st.number_input("実現したい年数", min_value=1, max_value=20, value=3)

        if st.button("次へ"):
            if st.session_state.goal:
                st.session_state.step += 1
            else:
                st.warning("目指す姿を入力してください。")

    # STEP 2
    elif st.session_state.step == 2:
        st.header("STEP 2：現在の職務経歴を入力")
        st.session_state.resume_text = st.text_area("職務経歴をここに貼り付けてください", height=300)

        uploaded_file = st.file_uploader("または、職務経歴書（PDF）をアップロード", type=["pdf"])

        if st.button("次へ", key="next2"):
            if st.session_state.resume_text or uploaded_file:
                st.session_state.step += 1
            else:
                st.warning("職務経歴を入力するか、PDFをアップロードしてください。")

    # STEP 3
    elif st.session_state.step == 3:
        st.header("STEP 3：アピールしたい軸を選択")
        st.session_state.appeal_axis = st.selectbox(
            "どの軸を一番アピールしたいですか？",
            ["課題解決力", "技術力", "提案力", "調整力", "学習力"]
        )

        if st.button("職務経歴書を生成"):
            st.session_state.step += 1
