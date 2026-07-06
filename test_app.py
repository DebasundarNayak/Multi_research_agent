import streamlit as st

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔬",
    layout="wide",
)

st.title("🔬 AI Research Agent")
st.write("Test app - if you see this, the app is working!")

st.sidebar.header("Menu")
st.sidebar.write("This is the sidebar")

research_topic = st.text_input("Enter a research topic:")
if st.button("Start Research"):
    st.success(f"Would research: {research_topic}")
