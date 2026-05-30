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
import streamlit as st
books = [
    {"title":"Python Dasar","author":"Archivio Team","category":"Programming"},
    {"title":"Python Advanced","author":"Tech Academy","category":"Programming"},
    {"title":"AI Modern","author":"Tech Publisher","category":"Artificial Intelligence"},
    {"title":"Machine Learning Essentials","author":"AI Institute","category":"Artificial Intelligence"},
    {"title":"Data Science 101","author":"Smart Academy","category":"Data Science"},
    {"title":"Deep Learning Guide","author":"AI Institute","category":"Data Science"},
    {"title":"Web Development","author":"Code School","category":"Web Development"},
    {"title":"HTML & CSS Mastery","author":"Frontend Academy","category":"Web Development"},
    {"title":"Cyber Security Fundamentals","author":"Secure Labs","category":"Cyber Security"},
    {"title":"Ethical Hacking","author":"Secure Labs","category":"Cyber Security"},
    {"title":"Database Management","author":"Data Press","category":"Database"},
    {"title":"Cloud Computing","author":"Cloud Academy","category":"Cloud"},
]
if "cart" not in st.session_state:
    st.session_state.cart = []

st.title("🔎 Explore Books")

search = st.text_input("Search")

for book in books:
    if search.lower() in book["title"].lower():
        with st.container(border=True):
            st.subheader(book["title"])
            st.write(book["author"])
            st.caption(book["category"])

            if st.button(f"Borrow {book['title']}", key=book["title"]):
                if len(st.session_state.cart) < 3:
                    if book["title"] not in st.session_state.cart:
                        st.session_state.cart.append(book["title"])
                        st.success("Added")
                else:
                    st.error("Borrow limit reached")
                    import streamlit as st

if "cart" not in st.session_state:
    st.session_state.cart = []

if "history" not in st.session_state:
    st.session_state.history = []

st.title("📖 My Books")

if not st.session_state.cart:
    st.info("No books borrowed.")
else:
    for book in st.session_state.cart[:]:
        col1,col2 = st.columns([4,1])

        with col1:
            st.write(book)

        with col2:
            if st.button("Return", key=book):
                st.session_state.cart.remove(book)
                st.rerun()

    if st.button("Checkout"):
        st.session_state.history.extend(st.session_state.cart)
        st.session_state.cart.clear()
        st.success("Checkout complete")
        import streamlit as st

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🕒 History")

if not st.session_state.history:
    st.info("No borrowing history.")
else:
    for item in st.session_state.history:
        st.write("📚", item)
        
import streamlit as st

st.title("ℹ️ About SmartLib Archivio")

st.markdown("""
### SmartLib Archivio

SmartLib Archivio is a digital library application designed to help users
discover, borrow, and manage books efficiently.

**Established:** June 4, 2020

The platform focuses on a clean user experience,
simple book management, and modern digital access.
""")


                    
