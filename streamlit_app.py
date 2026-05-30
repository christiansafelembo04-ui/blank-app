
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

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #020617 0%, #0f172a 40%, #172554 100%);
    color: white;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

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

.hero-title {
    font-size: 60px;
    font-weight: 700;
    line-height: 1.1;
    color: white;
}

.hero-title span {
    color: #22d3ee;
}

.hero-sub {
    color: #cbd5e1;
    margin-top: 20px;
    font-size: 18px;
}

/* METRIC CARD */
.metric-card {
    background: rgba(255,255,255,0.05);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

/* BUTTON */
.stButton > button {
    background: linear-gradient(135deg,#22d3ee,#2563eb);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 600;
    padding: 10px 20px;
}

.stButton > button:hover {
    color: white;
    border: none;
}

/* INFO */
.stAlert {
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE
# ==========================================
if "cart" not in st.session_state:
    st.session_state.cart = []

if "history" not in st.session_state:
    st.session_state.history = []

# ==========================================
# HERO SECTION
# ==========================================

left, right = st.columns([2,1])

with left:

    st.markdown("""
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
    """, unsafe_allow_html=True)

with right:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2232/2232688.png",
        width=320
    )

# ==========================================
# STATS
# ==========================================

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>📚 Books Borrowed</h3>
        <h1>{len(st.session_state.cart)}</h1>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <h3>📦 Borrow Limit</h3>
        <h1>3 Books</h1>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <h3>🕒 History Records</h3>
        <h1>{len(st.session_state.history)}</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# POPULAR CATEGORIES
# ==========================================

st.subheader("🔥 Popular Categories")

p1,p2,p3,p4,p5 = st.columns(5)

p1.button("Python")
p2.button("AI")
p3.button("Data Science")
p4.button("Cyber Security")
p5.button("Web Dev")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# INFO
# ==========================================

st.info(
    "Use the sidebar to open Explore, My Books, History, and About pages."
)


