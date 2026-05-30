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
# CUSTOM CSS
# ==========================================
st.markdown("""
<style>

/* GLOBAL */
html, body {
    font-family: 'Segoe UI', sans-serif;
    color: white;
}

/* MAIN BACKGROUND */
.stApp {
    background:
    linear-gradient(
        135deg,
        #071026,
        #0a1931,
        #111c44
    );
}

/* REMOVE TOP SPACE */
.block-container {
    padding-top: 2rem;
}

/* HERO */
.hero {
    background:
    linear-gradient(
        135deg,
        #0f1b3d,
        #101f54
    );

    padding: 40px;

    border-radius: 25px;

    border: 1px solid rgba(255,255,255,0.08);

    box-shadow:
    0 0 30px rgba(0,198,255,0.12);

    margin-bottom: 35px;
}

/* MAIN TITLE */
.main-title {
    font-size: 52px;
    font-weight: 800;
    color: white;
}

/* BLUE TEXT */
.blue {
    color: #00cfff;
    text-shadow:
    0 0 8px rgba(0,207,255,0.35);
}

/* HERO TITLE */
.hero-title {
    font-size: 58px;
    font-weight: 900;
    color: white;
    margin-top: 20px;
    line-height: 1.1;
}

/* HERO DESC */
.hero-desc {
    font-size: 20px;
    color: #dbeafe;
    margin-top: 18px;
}

/* SEARCH */
.stTextInput input {

    background-color: #0b1736 !important;

    color: white !important;

    border-radius: 14px !important;

    border: 1px solid rgba(0,198,255,0.25) !important;

    padding: 12px !important;

    font-size: 16px !important;
}

/* BUTTON */
.stButton button {

    background:
    linear-gradient(
        90deg,
        #00c6ff,
        #6f42ff
    );

    color: white;

    border: none;

    border-radius: 12px;

    padding: 10px 18px;

    font-weight: bold;

    transition: 0.3s;

    box-shadow:
    0 0 15px rgba(0,198,255,0.15);
}

.stButton button:hover {

    transform: translateY(-2px);

    box-shadow:
    0 0 20px rgba(0,198,255,0.28);
}

/* METRIC BOX */
.metric-box {

    background:
    rgba(20,30,70,0.9);

    padding: 24px;

    border-radius: 20px;

    text-align: center;

    border: 1px solid rgba(255,255,255,0.06);

    transition: 0.3s;
}

.metric-box:hover {

    transform: translateY(-4px);

    box-shadow:
    0 0 25px rgba(0,198,255,0.18);
}

/* METRIC ICON */
.metric-icon {

    font-size: 34px;

    margin-bottom: 10px;

    filter:
    drop-shadow(0 0 8px #00cfff);
}

/* METRIC TITLE */
.metric-title {

    color: #dbeafe;

    font-size: 22px;

    font-weight: 700;
}

/* METRIC VALUE */
.metric-value {

    color: white;

    font-size: 52px;

    font-weight: 900;

    margin-top: 8px;
}

/* METRIC SUB */
.metric-sub {

    color: #93c5fd;

    font-size: 13px;

    margin-top: 6px;
}

/* BOOK CARD */
.book-card {

    background:
    rgba(15,25,60,0.95);

    padding: 20px;

    border-radius: 20px;

    margin-bottom: 20px;

    border: 1px solid rgba(255,255,255,0.08);

    transition: 0.3s;
}

.book-card:hover {

    transform: translateY(-4px);

    box-shadow:
    0 0 25px rgba(0,198,255,0.20);
}

/* BOOK TITLE */
.book-title {

    color: white;

    font-size: 32px;

    font-weight: 800;
}

/* AUTHOR */
.author {

    color: #dbeafe;

    font-size: 17px;
}

/* CATEGORY TAG */
.tag {

    display: inline-block;

    padding: 6px 14px;

    border-radius: 999px;

    background:
    rgba(111,66,255,0.25);

    color: #dbeafe;

    font-size: 13px;

    margin-top: 10px;
}

/* IMAGE */
img {
    border-radius: 18px !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #081225;
}

</style>
""", unsafe_allow_html=True)

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
    },
    {
        "title":"Cyber Security",
        "author":"Secure Labs",
        "category":"Cyber Security",
        "image":"https://images.unsplash.com/photo-1510511459019-5dda7724fd87"
    }
]

# ==========================================
# HERO
# ==========================================
st.markdown("""
<div class="hero">

<div class="main-title">
📚 SmartLib <span class="blue">Archivio</span>
</div>

<div class="hero-title">
Find Your Favorite Book <span class="blue">Instantly</span>
</div>

<div class="hero-desc">
Search thousands of books with a modern digital library experience.
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
        Borrowed
        </div>

        <div class="metric-value">
        {len(st.session_state.cart)}
        </div>

        <div class="metric-sub">
        Active borrowed books
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

        <div class="metric-sub">
        Maximum allowed books
        </div>

    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-box">

        <div class="metric-icon">🕒</div>

        <div class="metric-title">
        History
        </div>

        <div class="metric-value">
        {len(st.session_state.history)}
        </div>

        <div class="metric-sub">
        Borrowing records
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
# BOOK LIST
# ==========================================
for book in books:

    if search.lower() in book["title"].lower():

        col1, col2 = st.columns([1,4])

        with col1:
            st.image(book["image"], use_container_width=True)

        with col2:

            st.markdown(f"""
            <div class="book-card">

            <div class="book-title">
                {book["title"]}
            </div>

            <br>

            <p class="author">
                Author: {book["author"]}
            </p>

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

# ==========================================
# MY BOOKS
# ==========================================
st.divider()

st.header("📖 My Books")

if not st.session_state.cart:
    st.info("No books borrowed.")

else:

    for item in st.session_state.cart:
        st.success(f"✅ {item}")

# ==========================================
# HISTORY
# ==========================================
st.divider()

st.header("🕒 History")

if not st.session_state.history:
    st.info("No borrowing history.")

else:

    for item in st.session_state.history:
        st.write(f"📚 {item}")
