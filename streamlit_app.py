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
    radial-gradient(circle at top left, rgba(0,198,255,0.15), transparent 25%),
    radial-gradient(circle at bottom right, rgba(111,66,255,0.15), transparent 25%),
    linear-gradient(135deg,#050816,#081327,#0c1f47);
}

/* REMOVE TOP SPACE */
.block-container {
    padding-top: 2rem;
}

/* HERO SECTION */
.hero {
    background:
    linear-gradient(
        145deg,
        rgba(10,20,60,0.96),
        rgba(15,25,70,0.96)
    );

    padding: 50px;
    border-radius: 28px;

    border: 1px solid rgba(255,255,255,0.06);

    box-shadow:
        0 0 40px rgba(0,198,255,0.12);

    margin-bottom: 35px;
}

/* MAIN TITLE */
.main-title {
    font-size: 58px;
    font-weight: 900;
    color: white;
}

.blue {
    color: #00cfff;
    text-shadow: 0 0 12px rgba(0,207,255,0.7);
}

/* HERO TITLE */
.hero-title {
    font-size: 68px;
    font-weight: 900;
    line-height: 1.1;
    color: white;
    margin-top: 20px;
}

/* HERO DESC */
.hero-desc {
    color: #dbeafe;
    font-size: 22px;
    margin-top: 20px;
}

/* SEARCH BOX */
.stTextInput input {

    background: rgba(15,25,60,0.95) !important;

    color: white !important;

    border-radius: 16px !important;

    border: 1px solid rgba(0,198,255,0.25) !important;

    padding: 14px !important;

    font-size: 16px !important;
}

/* BUTTON */
.stButton button {

    background:
    linear-gradient(90deg,#00c6ff,#6f42ff);

    color: white;

    border: none;

    border-radius: 14px;

    padding: 10px 22px;

    font-weight: 700;

    transition: 0.3s;

    box-shadow:
    0 0 18px rgba(0,198,255,0.25);
}

.stButton button:hover {

    transform: translateY(-3px);

    box-shadow:
    0 0 25px rgba(0,198,255,0.5),
    0 0 40px rgba(111,66,255,0.3);
}

/* METRIC BOX */
.metric-box {

    background:
    linear-gradient(
        145deg,
        rgba(15,25,60,0.96),
        rgba(10,20,55,0.95)
    );

    padding: 28px;

    border-radius: 24px;

    border: 1px solid rgba(0,198,255,0.12);

    text-align: center;

    transition: 0.35s;

    box-shadow:
    0 0 25px rgba(0,198,255,0.08);
}

.metric-box:hover {

    transform: translateY(-6px);

    box-shadow:
    0 0 35px rgba(0,198,255,0.22),
    0 0 55px rgba(111,66,255,0.14);
}

/* METRIC ICON */
.metric-icon {

    font-size: 42px;

    margin-bottom: 10px;

    filter:
    drop-shadow(0 0 8px #00cfff)
    drop-shadow(0 0 16px #6f42ff);
}

/* METRIC TITLE */
.metric-title {

    color: white;

    font-size: 24px;

    font-weight: 700;

    margin-bottom: 12px;
}

/* METRIC VALUE */
.metric-value {

    color: white;

    font-size: 56px;

    font-weight: 900;

    text-shadow:
    0 0 15px rgba(0,198,255,0.35);
}

/* METRIC SUBTEXT */
.metric-sub {

    color: #93c5fd;

    margin-top: 10px;

    font-size: 14px;
}

/* BOOK CARD */
.book-card {

    background:
    linear-gradient(
        145deg,
        rgba(10,20,60,0.95),
        rgba(14,24,64,0.95)
    );

    padding: 24px;

    border-radius: 24px;

    margin-bottom: 20px;

    border: 1px solid rgba(255,255,255,0.06);

    transition: 0.35s;

    box-shadow:
    0 0 20px rgba(0,0,0,0.25);
}

.book-card:hover {

    transform: translateY(-5px);

    border: 1px solid rgba(0,198,255,0.3);

    box-shadow:
    0 0 30px rgba(0,198,255,0.18);
}

/* BOOK TITLE */
.book-title {

    color: white;

    font-size: 34px;

    font-weight: 800;
}

/* AUTHOR */
.author {

    color: #dbeafe;

    font-size: 18px;
}

/* CATEGORY TAG */
.tag {

    display: inline-block;

    padding: 7px 16px;

    border-radius: 999px;

    background:
    linear-gradient(
        90deg,
        rgba(111,66,255,0.25),
        rgba(0,198,255,0.2)
    );

    color: #dbeafe;

    font-size: 14px;

    margin-top: 10px;

    border: 1px solid rgba(255,255,255,0.06);
}

/* IMAGE */
img {
    border-radius: 18px !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #050b18,
        #081225
    );
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
