
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
