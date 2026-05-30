import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="SmartLib Archivio",
    page_icon="📚",
    layout="wide"
)

# ==========================================
# SESSION STATE
# ==========================================
if "cart" not in st.session_state:
    st.session_state.cart = []

if "history" not in st.session_state:
    st.session_state.history = []

# ==========================================
# BOOK DATA
# ==========================================
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

# ==========================================
# HEADER
# ==========================================
st.title("📚 SmartLib Archivio")
st.subheader("Find Your Favorite Book Instantly")

st.markdown("""
### Welcome
SmartLib Archivio is a modern digital library platform.

Use this application to:
- Explore books
- Borrow books
- Return books
- View borrowing history
""")

# ==========================================
# METRICS
# ==========================================
c1, c2, c3 = st.columns(3)

c1.metric("Books Borrowed", len(st.session_state.cart))
c2.metric("Borrow Limit", "3 Books")
c3.metric("History Records", len(st.session_state.history))

# ==========================================
# EXPLORE BOOKS
# ==========================================
st.divider()
st.header("🔎 Explore Books")

search = st.text_input("Search Book")

for book in books:
    if search.lower() in book["title"].lower():

        with st.container(border=True):

            st.subheader(book["title"])
            st.write(f"Author: {book['author']}")
            st.caption(book["category"])

            if st.button(
                f"Borrow {book['title']}",
                key=f"borrow_{book['title']}"
            ):

                if len(st.session_state.cart) < 3:

                    if book["title"] not in st.session_state.cart:
                        st.session_state.cart.append(book["title"])
                        st.success("Book added successfully")

                    else:
                        st.warning("Book already borrowed")

                else:
                    st.error("Borrow limit reached")

# ==========================================
# MY BOOKS
# ==========================================
st.divider()
st.header("📖 My Books")

if not st.session_state.cart:
    st.info("No books borrowed.")

else:

    for book in st.session_state.cart[:]:

        col1, col2 = st.columns([4,1])

        with col1:
            st.write(book)

        with col2:
            if st.button("Return", key=f"return_{book}"):

                st.session_state.cart.remove(book)
                st.rerun()

    if st.button("Checkout"):

        st.session_state.history.extend(st.session_state.cart)
        st.session_state.cart.clear()

        st.success("Checkout complete")

# ==========================================
# HISTORY
# ==========================================
st.divider()
st.header("🕒 History")

if not st.session_state.history:
    st.info("No borrowing history.")

else:
    for item in st.session_state.history:
        st.write("📚", item)

# ==========================================
# ABOUT
# ==========================================
st.divider()
st.header("ℹ️ About SmartLib Archivio")

st.markdown("""
### SmartLib Archivio

SmartLib Archivio is a digital library application designed to help users
discover, borrow, and manage books efficiently.

**Established:** June 4, 2020

The platform focuses on:
- Clean user experience
- Simple book management
- Modern digital access
""")
