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

# ==========================================
# CUSTOM CSS
# ==========================================
st.markdown("""
<style>

/* =========================
GLOBAL
========================= */

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.stApp {
    background:
    radial-gradient(circle at top left, rgba(0,198,255,0.15), transparent 25%),
    radial-gradient(circle at bottom right, rgba(111,66,255,0.15), transparent 25%),
    linear-gradient(135deg,#020617,#081127,#0c1d48);

    color: white;
}

/* =========================
REMOVE STREAMLIT STYLE
========================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* =========================
NAVBAR
========================= */

.navbar {

    background:
    rgba(10,15,40,0.95);

    border: 1px solid rgba(255,255,255,0.06);

    padding: 14px 30px;

    border-radius: 18px;

    margin-bottom: 25px;

    display: flex;

    justify-content: space-between;

    align-items: center;

    box-shadow:
    0 0 25px rgba(0,198,255,0.08);
}

.logo {

    font-size: 34px;

    font-weight: 800;

    color: white;
}

.logo span {
    color: #00cfff;
}

.menu {

    display: flex;

    gap: 30px;

    font-size: 16px;
}

.menu a {

    color: #dbeafe;

    text-decoration: none;

    transition: 0.3s;
}

.menu a:hover {
    color: #00cfff;
}

/* =========================
HERO
========================= */

.hero {

    background:
    linear-gradient(
        145deg,
        rgba(10,20,60,0.95),
        rgba(15,25,70,0.95)
    );

    border-radius: 30px;

    padding: 50px;

    border: 1px solid rgba(255,255,255,0.06);

    box-shadow:
    0 0 40px rgba(0,198,255,0.12);

    margin-bottom: 30px;
}

.hero-title {

    font-size: 70px;

    font-weight: 900;

    line-height: 1.1;

    color: white;
}

.glow {
    color: #00cfff;

    text-shadow:
    0 0 10px rgba(0,207,255,0.7),
    0 0 20px rgba(0,207,255,0.4);
}

.hero-desc {

    color: #dbeafe;

    font-size: 22px;

    margin-top: 18px;
}

/* =========================
SEARCH BOX
========================= */

.stTextInput input {

    background:
    rgba(10,20,55,0.95) !important;

    color: white !important;

    border-radius: 18px !important;

    border: 1px solid rgba(0,198,255,0.25) !important;

    padding: 15px !important;

    font-size: 16px !important;
}

/* =========================
BOOK CARD
========================= */

.book-card {

    background:
    linear-gradient(
        145deg,
        rgba(10,20,60,0.95),
        rgba(15,25,70,0.95)
    );

    border-radius: 24px;

    padding: 22px;

    margin-bottom: 22px;

    border: 1px solid rgba(255,255,255,0.06);

    box-shadow:
    0 0 20px rgba(0,0,0,0.2);

    transition: 0.3s;
}

.book-card:hover {

    transform: translateY(-4px);

    box-shadow:
    0 0 30px rgba(0,198,255,0.18);
}

/* =========================
BOOK TITLE
========================= */

.book-title {

    color: white;

    font-size: 34px;

    font-weight: 800;
}

/* =========================
AUTHOR
========================= */

.author {

    color: #dbeafe;

    font-size: 18px;
}

/* =========================
TAG
========================= */

.tag {

    display: inline-block;

    margin-top: 12px;

    padding: 7px 16px;

    border-radius: 999px;

    background:
    linear-gradient(
        90deg,
        rgba(111,66,255,0.25),
        rgba(0,198,255,0.25)
    );

    color: #dbeafe;

    font-size: 13px;
}

/* =========================
BUTTON
========================= */

.stButton button {

    background:
    linear-gradient(
        90deg,
        #00c6ff,
        #6f42ff
    );

    color: white;

    border: none;

    border-radius: 14px;

    padding: 11px 24px;

    font-weight: 700;

    transition: 0.3s;

    box-shadow:
    0 0 18px rgba(0,198,255,0.2);
}

.stButton button:hover {

    transform: translateY(-3px);

    box-shadow:
    0 0 25px rgba(0,198,255,0.35);
}

/* =========================
METRICS
========================= */

.metric-box {

    background:
    linear-gradient(
        145deg,
        rgba(15,25,60,0.95),
        rgba(12,22,55,0.95)
    );

    border-radius: 24px;

    padding: 30px;

    text-align: center;

    border: 1px solid rgba(255,255,255,0.06);

    box-shadow:
    0 0 25px rgba(0,198,255,0.08);
}

.metric-icon {

    font-size: 42px;

    margin-bottom: 12px;
}

.metric-title {

    color: #dbeafe;

    font-size: 24px;

    font-weight: 700;
}

.metric-value {

    color: white;

    font-size: 56px;

    font-weight: 900;

    margin-top: 10px;
}

/* =========================
IMAGE
========================= */

img {
    border-radius: 18px !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# NAVBAR
# ==========================================
st.markdown("""
<div class="navbar">

<div class="logo">
📚 SmartLib <span>Archivio</span>
</div>

<div class="menu">
<a href="#">Home</a>
<a href="#">Explore</a>
<a href="#">My Books</a>
<a href="#">History</a>
<a href="#">About</a>
</div>

</div>
""", unsafe_allow_html=True)

# ==========================================
# HERO SECTION
# ==========================================
st.markdown("""
<div class="hero">

<div class="hero-title">
Find Your Favorite Book
<span class="glow">Instantly</span>
</div>

<div class="hero-desc">
Search thousands of books with a fast and efficient system.
</div>

</div>
""", unsafe_allow_html=True)

# ==========================================
# METRICS
# ==========================================
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="metric-box">

    <div class="metric-icon">📚</div>

    <div class="metric-title">
    Books Borrowed
    </div>

    <div class="metric-value">
    {len(st.session_state.cart)}
    </div>

    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-box">

    <div class="metric-icon">🛡️</div>

    <div class="metric-title">
    Borrow Limit
    </div>

    <div class="metric-value">
    3 Books
    </div>

    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-box">

    <div class="metric-icon">🕒</div>

    <div class="metric-title">
    History
    </div>

    <div class="metric-value">
    0
    </div>

    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# SEARCH
# ==========================================
search = st.text_input("🔎 Search books")

# ==========================================
# BOOK DATA
# ==========================================
books = [
    {
        "title":"Python Dasar",
        "author":"Archivio Team",
        "category":"Programming",
        "image":"https://images.unsplash.com/photo-1515879218367-8466d910aaa4"
    },
    {
        "title":"AI Modern",
        "author":"Tech Publisher",
        "category":"Artificial Intelligence",
        "image":"https://images.unsplash.com/photo-1677442136019-21780ecad995"
    },
    {
        "title":"Data Science 101",
        "author":"Smart Academy",
        "category":"Data Science",
        "image":"https://images.unsplash.com/photo-1551288049-bebda4e38f71"
    }
]

# ==========================================
# BOOK LIST
# ==========================================
for book in books:

    if search.lower() in book["title"].lower():

        col1, col2 = st.columns([1,4])

        with col1:
            st.image(
                book["image"],
                use_container_width=True
            )

        with col2:

            st.markdown(f"""
            <div class="book-card">

            <div class="book-title">
            {book["title"]}
            </div>

            <br>

            <div class="author">
            Author: {book["author"]}
            </div>

            <div class="tag">
            {book["category"]}
            </div>

            </div>
            """, unsafe_allow_html=True)

            if st.button(
                f"Borrow {book['title']}",
                key=book["title"]
            ):

                if len(st.session_state.cart) < 3:

                    if book["title"] not in st.session_state.cart:

                        st.session_state.cart.append(book["title"])

                        st.success("Book added successfully")

                    else:
                        st.warning("Book already borrowed")

                else:
                    st.error("Borrow limit reached")
