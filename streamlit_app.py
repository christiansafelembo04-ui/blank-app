
import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="SmartLib Archivio",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
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

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* BACKGROUND */
.stApp {
    background: linear-gradient(
        135deg,
        #020617 0%,
        #0f172a 40%,
        #172554 100%
    );
    color: white;
}

/* HIDE DEFAULT */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: rgba(15,23,42,0.95);
}

/* PAGE */
.block-container {
    padding-top: 2rem;
    max-width: 95%;
}

/* HERO */
.hero {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 30px;
    padding: 50px;
    margin-bottom: 30px;
}

/* HERO TITLE */
.hero-title {
    font-size: 64px;
    font-weight: 700;
    line-height: 1.1;
    color: white;
}

.hero-title span {
    color: #22d3ee;
}

/* HERO SUB */
.hero-sub {
    color: #cbd5e1;
    margin-top: 20px;
    font-size: 18px;
    line-height: 1.8;
}

/* CARD */
.metric-card {
    background: rgba(255,255,255,0.05);
    border-radius: 24px;
    padding: 30px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

/* NUMBER */
.metric-number {
    font-size: 55px;
    font-weight: 700;
    color: white;
}

/* BUTTON */
.stButton > button {
    background: linear-gradient(
        135deg,
        #22d3ee,
        #2563eb
    );

    color: white;
    border: none;
    border-radius: 14px;
    padding: 12px 20px;
    font-weight: 600;
    width: 100%;
}

.stButton > button:hover {
    color: white;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HERO SECTION
# ==========================================

left, right = st.columns([2,1])

hero_html = """
<div class="hero">

    <div class="hero-title">
        Find Your Favorite Book
        <span>Instantly</span>
    </div>

    <div class="hero-sub">
        SmartLib Archivio is a modern digital library platform
        designed to help users discover, borrow, and manage
        books efficiently.
    </div>

</div>
"""

with left:
    st.markdown(hero_html, unsafe_allow_html=True)

with right:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/2232/2232688.png",
        width=320
    )

# ==========================================
# STATS
# ==========================================

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown(f"""
    <div class="metric-card">
        <h2>📚 Books Borrowed</h2>
        <div class="metric-number">
            {len(st.session_state.cart)}
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="metric-card">
        <h2>📦 Borrow Limit</h2>
        <div class="metric-number">
            3
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:

    st.markdown(f"""
    <div class="metric-card">
        <h2>🕒 History Records</h2>
        <div class="metric-number">
            {len(st.session_state.history)}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# SPACE
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# POPULAR CATEGORY
# ==========================================

st.subheader("🔥 Popular Categories")

p1, p2, p3, p4, p5 = st.columns(5)

with p1:
    st.button("Python")

with p2:
    st.button("AI")

with p3:
    st.button("Data Science")

with p4:
    st.button("Cyber Security")

with p5:
    st.button("Web Dev")

# ==========================================
# INFO
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

st.sidebar.title("📚 Navigation")

st.sidebar.success("Select a page below.")

st.markdown("""
<div style="
    background: rgba(255,255,255,0.05);
    padding: 18px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.08);
    color: #cbd5e1;
    margin-top: 20px;
">
    📌 Use the sidebar navigation to explore pages like
    <b>Explore</b>, <b>My Books</b>, <b>History</b>, and <b>About</b>.
</div>
""", unsafe_allow_html=True)
