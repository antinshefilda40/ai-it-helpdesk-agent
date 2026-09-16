import streamlit as st
from src.agent import run_agent

st.set_page_config(page_title="AI IT Helpdesk Agent", page_icon="🛠️", layout="centered")
st.title("🛠️ AI IT Helpdesk Agent")
st.caption("Agent + RAG + Tools | Student project prototype")

question = st.text_area(
    "Describe your IT problem",
    placeholder="Example: My Wi-Fi is connected but I cannot access the internet.",
    height=120,
)

if st.button("Get Help", type="primary") and question.strip():
    result = run_agent(question.strip())
    st.subheader("Agent Response")
    st.write(result["response"])

    if result["tool"]:
        st.subheader("Tool Used")
        st.code(result["tool"])

    if result["sources"]:
        st.subheader("Knowledge Sources")
        for source in result["sources"]:
            st.write(f"- {source}")

st.divider()
st.info("Demo only: diagnostic and ticket tools are simulations and do not change your computer.")
