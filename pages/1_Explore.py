```python
import streamlit as st

# ==========================================
# SESSION STATE
# ==========================================

if "cart" not in st.session_state:
    st.session_state.cart = []

# ==========================================
# BOOK DATABASE
# ==========================================

books = [
    {
        "title":"Python Dasar",
        "author":"Archivio Team",
        "category":"Programming",
        "description":"Belajar Python dari dasar hingga mahir."
    },

    {
        "title":"Python Advanced",
        "author":"Tech Academy",
        "category":"Programming",
        "description":"Teknik Python tingkat lanjut untuk developer."
    },

    {
        "title":"AI Modern",
        "author":"Tech Publisher",
        "category":"Artificial Intelligence",
        "description":"Panduan memahami AI modern."
    },

    {
        "title":"Machine Learning Essentials",
        "author":"AI Institute",
        "category":"Artificial Intelligence",
        "description":"Dasar machine learning dan implementasi."
    },

    {
        "title":"Data Science 101",
        "author":"Smart Academy",
        "category":"Data Science",
        "description":"Belajar data science menggunakan Python."
    },

    {
        "title":"Deep Learning Guide",
        "author":"AI Institute",
        "category":"Data Science",
        "description":"Pelajari neural network dan deep learning."
    },

    {
        "title":"Web Development",
        "author":"Code School",
        "category":"Web Development",
        "description":"Panduan membuat website modern."
    },

    {
        "title":"Cyber Security Fundamentals",
        "author":"Secure Labs",
        "category":"Cyber Security",
        "description":"Belajar keamanan digital dan jaringan."
    }
]

# ==========================================
# PAGE TITLE
# ==========================================

st.title("🔎 Explore Books")

st.markdown("""
Cari buku favoritmu dan tambahkan ke cart peminjaman.
""")

# ==========================================
# SEARCH
# ==========================================

search = st.text_input(
    "Search Books",
    placeholder="Search by title, author, or category..."
)

# ==========================================
# FILTER
# ==========================================

filtered_books = []

for book in books:

    if (
        search.lower() in book["title"].lower()
        or search.lower() in book["author"].lower()
        or search.lower() in book["category"].lower()
    ):

        filtered_books.append(book)

# ==========================================
# BOOK DISPLAY
# ==========================================

for book in filtered_books:

    with st.container(border=True):

        left, right = st.columns([4,1])

        with left:

            st.subheader(book["title"])

            st.write(f"👤 {book['author']}")

            st.caption(f"📚 {book['category']}")

            st.write(book["description"])

        with right:

            st.markdown("<br>", unsafe_allow_html=True)

            if st.button(
                "Borrow",
                key=book["title"],
                use_container_width=True
            ):

                if len(st.session_state.cart) >= 3:

                    st.error("Borrow limit reached!")

                else:

                    if book["title"] not in st.session_state.cart:

                        st.session_state.cart.append(book["title"])

                        st.success(f"{book['title']} added!")

                    else:

                        st.warning("Book already borrowed.")
```
