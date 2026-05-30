
import streamlit as st

st.set_page_config(page_title="SmartLib Archivio", page_icon="📚", layout="wide")

if "cart" not in st.session_state:
    st.session_state.cart = []
if "history" not in st.session_state:
    st.session_state.history = []

st.title("📚 SmartLib Archivio")
st.subheader("Find Your Favorite Book Instantly")

st.markdown("""
### Welcome
SmartLib Archivio is a modern digital library platform.
Use the sidebar pages to explore books, manage borrowed books,
view history, and learn more about the project.
""")

c1,c2,c3 = st.columns(3)
c1.metric("Books Borrowed", len(st.session_state.cart))
c2.metric("Borrow Limit", "3 Books")
c3.metric("History Records", len(st.session_state.history))

st.info("Open the pages in the sidebar: Explore, My Books, History, and About.")
