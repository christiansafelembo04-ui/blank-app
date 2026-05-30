import streamlit as st

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🕒 History")

if not st.session_state.history:
    st.info("No borrowing history.")
else:
    for item in st.session_state.history:
        st.write("📚", item)
