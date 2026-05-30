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
# CUSTOM CSS
# ==========================================
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    background-color: #071026;
    color: white;
}

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(135deg,#071026,#0a1931,#111c44);
}

/* TITLE */
.main-title {
    font-size: 52px;
    font-weight: 800;
    color: white;
}

.blue {
    color: #00c6ff;
}

/* HERO BOX */
.hero {
    background: linear-gradient(135deg,#0f1b3d,#101f54);
    padding: 40px;
    border-radius: 25px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 0 30px rgba(0,198,255,0.15);
}

/* SEARCH BOX */
.stTextInput input {
    background-color: #0b1736;
    color: white;
    border-radius: 14px;
    border: 1px solid #2f4fff;
    padding: 12px;
}

/* BUTTON */
.stButton button {
    background: linear-gradient(90deg,#00c6ff,#6f42ff);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.04);
    box-shadow: 0 0 15px #00c6ff;
}

/* BOOK CARD */
.book-card {
    background: rgba(15,25,60,0.95);
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    transition: 0.3s;
}

.book-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 0 25px rgba(0,198,255,0.25);
}

/* CATEGORY TAG */
.tag {
    display:inline-block;
    padding:6px 14px;
    border-radius:999px;
    background: rgba(111,66,255,0.25);
    color:#b892ff;
    font-size:13px;
    margin-top:8px;
}

/* METRIC */
.metric-box {
    background: rgba(20,30,70,0.9);
    padding: 20px;
    border-radius: 18px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.06);
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #081225;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION
# ==========================================
if "cart" not in st.session_state:
    st.session_state.cart = []

if "history" not in st.session_state:
    st.session_state.history = []

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
# HERO SECTION
# ==========================================
st.markdown("""
<div class="hero">

<div class="main-title">
📚 SmartLib <span class="blue">Archivio</span>
</div>

<h1 style="font-size:58px;margin-top:20px;">
Find Your Favorite Book <span class="blue">Instantly</span>
</h1>

<p style="font-size:20px;color:#cbd5e1;">
Search thousands of books with a modern digital library experience.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================
# METRICS
# ==========================================
c1,c2,c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="metric-box">
        <h3>📚 Borrowed</h3>
        <h1>{len(st.session_state.cart)}</h1>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-box">
        <h3>🛡 Borrow Limit</h3>
        <h1>3 Books</h1>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-box">
        <h3>🕒 History</h3>
        <h1>{len(st.session_state.history)}</h1>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# SEARCH
# ==========================================
search = st.text_input("🔎 Search books")

# ==========================================
# BOOKS
# ==========================================
for book in books:

    if search.lower() in book["title"].lower():

        col1,col2 = st.columns([1,4])

        with col1:
            st.image(book["image"], use_container_width=True)

        with col2:

            st.markdown(f"""
            <div class="book-card">

            <h2>{book["title"]}</h2>

            <p style="color:#cbd5e1;">
            Author: {book["author"]}
            </p>

            <div class="tag">
            {book["category"]}
            </div>

            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Borrow {book['title']}", key=book["title"]):

                if len(st.session_state.cart) < 3:

                    if book["title"] not in st.session_state.cart:
                        st.session_state.cart.append(book["title"])
                        st.success("Book added successfully")

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
        st.write(item)
