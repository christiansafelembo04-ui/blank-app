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

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    color: white;
}

/* BACKGROUND */
.stApp {
    background:
    radial-gradient(circle at top left, #0b2c5f 0%, transparent 35%),
    radial-gradient(circle at bottom right, #182b7a 0%, transparent 35%),
    linear-gradient(135deg,#020617,#071026,#081b3a,#111c44);
}

/* HIDE STREAMLIT */
header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* NAVBAR */
.navbar {
    background: rgba(4,10,35,0.88);
    padding: 24px 40px;
    border-radius: 24px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:30px;
    border:1px solid rgba(255,255,255,0.06);
    box-shadow:0 0 40px rgba(0,198,255,0.08);
}

.logo {
    font-size:42px;
    font-weight:800;
    color:white;
}

.logo-blue {
    color:#00d9ff;
}

.nav-links {
    display:flex;
    gap:35px;
    font-size:18px;
    color:#cbd5e1;
}

/* HERO */
.hero {
    background: linear-gradient(135deg,#08144a,#0a1f63);
    padding: 70px;
    border-radius: 35px;
    border:1px solid rgba(255,255,255,0.08);
    box-shadow:0 0 60px rgba(0,198,255,0.12);
}

/* HERO TITLE */
.hero-title {
    font-size:88px;
    line-height:1;
    font-weight:900;
    margin-bottom:20px;
    color:white;
}

.glow {
    color:#00d9ff;

    text-shadow:
    0 0 10px #00d9ff,
    0 0 20px #00d9ff,
    0 0 40px #00d9ff,
    0 0 80px #00d9ff;
}

.hero-subtitle {
    font-size:24px;
    color:#cbd5e1;
    margin-top:25px;
}

/* ESTABLISHED */
.established-box {
    margin-top:40px;
    width:fit-content;
    padding:18px 24px;
    border-radius:20px;
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.08);
}

.established-title {
    font-size:30px;
    font-weight:800;
    color:white;
}

.established-sub {
    color:#94a3b8;
    font-size:17px;
    margin-top:8px;
}

/* METRIC */
.metric-box {
    background: rgba(8,20,70,0.88);
    padding: 45px 20px;
    border-radius: 28px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.05);
    transition:0.3s;
    box-shadow:0 0 30px rgba(0,198,255,0.08);
}

.metric-box:hover {
    transform:translateY(-6px);
    box-shadow:0 0 35px rgba(0,198,255,0.18);
}

.metric-icon {
    font-size:55px;
}

.metric-title {
    font-size:28px;
    font-weight:700;
    margin-top:20px;
}

.metric-number {
    font-size:72px;
    font-weight:900;
    margin-top:20px;
}

/* SEARCH */
.stTextInput input {
    background: rgba(10,20,50,0.95);
    color: white;
    border-radius: 18px;
    border: 1px solid #2f4fff;
    padding: 18px;
    font-size:18px;
}

/* BOOK CARD */
.book-card {
    background: rgba(12,20,55,0.92);
    padding: 28px;
    border-radius: 24px;
    margin-bottom: 24px;
    border:1px solid rgba(255,255,255,0.06);
    transition:0.3s;
}

.book-card:hover {
    transform:translateY(-5px);
    box-shadow:0 0 30px rgba(0,198,255,0.18);
}

/* TAG */
.tag {
    display:inline-block;
    margin-top:14px;
    padding:8px 18px;
    border-radius:999px;
    background:rgba(0,217,255,0.12);
    color:#00d9ff;
    font-size:14px;
    font-weight:600;
}

/* BUTTON */
.stButton button {
    width:100%;
    background: linear-gradient(90deg,#00c6ff,#6f42ff);
    color:white;
    border:none;
    border-radius:16px;
    padding:14px;
    font-size:16px;
    font-weight:700;
    transition:0.3s;
}

.stButton button:hover {
    transform:scale(1.03);
    box-shadow:0 0 25px #00d9ff;
}

/* SECTION TITLE */
.section-title {
    font-size:40px;
    font-weight:800;
    margin-top:20px;
    margin-bottom:20px;
}

/* HISTORY */
.history-box {
    background:rgba(10,20,55,0.9);
    padding:18px;
    border-radius:18px;
    margin-bottom:12px;
    border:1px solid rgba(255,255,255,0.05);
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
# NAVBAR
# ==========================================
st.markdown("""
<div class="navbar">

<div class="logo">
📚 SmartLib <span class="logo-blue">Archivio</span>
</div>

<div class="nav-links">
<span>Home</span>
<span>Explore</span>
<span>Borrow Cart</span>
<span>History</span>
<span>About</span>
</div>

</div>
""", unsafe_allow_html=True)

# ==========================================
# BOOK DATA
# ==========================================
books = [

    # HARRY POTTER
    {
        "title":"Harry Potter and the Sorcerer’s Stone",
        "author":"J.K. Rowling",
        "category":"Fantasy",
        "image":"https://images.unsplash.com/photo-1512820790803-83ca734da794"
    },

    {
        "title":"Harry Potter and the Chamber of Secrets",
        "author":"J.K. Rowling",
        "category":"Fantasy",
        "image":"https://images.unsplash.com/photo-1495446815901-a7297e633e8d"
    },

    {
        "title":"Harry Potter and the Prisoner of Azkaban",
        "author":"J.K. Rowling",
        "category":"Fantasy",
        "image":"https://images.unsplash.com/photo-1524578271613-d550eacf6090"
    },

    {
        "title":"Harry Potter and the Goblet of Fire",
        "author":"J.K. Rowling",
        "category":"Fantasy",
        "image":"https://images.unsplash.com/photo-1516979187457-637abb4f9353"
    },

    {
        "title":"Harry Potter and the Order of the Phoenix",
        "author":"J.K. Rowling",
        "category":"Fantasy",
        "image":"https://images.unsplash.com/photo-1544947950-fa07a98d237f"
    },

    # MARVEL & DC
    {
        "title":"Avengers: Endgame",
        "author":"Marvel Studios",
        "category":"Superhero",
        "image":"https://images.unsplash.com/photo-1531259683007-016a7b628fc3"
    },

    {
        "title":"Avengers: Infinity War",
        "author":"Marvel Studios",
        "category":"Superhero",
        "image":"https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c"
    },

    {
        "title":"The Amazing Spider-Man",
        "author":"Marvel Comics",
        "category":"Superhero",
        "image":"https://images.unsplash.com/photo-1635805737707-575885ab0820"
    },

    {
        "title":"Batman: The Dark Knight",
        "author":"DC Comics",
        "category":"Superhero",
        "image":"https://images.unsplash.com/photo-1608889175119-6c7d1d5d4d4a"
    },

    {
        "title":"Superman Returns",
        "author":"DC Comics",
        "category":"Superhero",
        "image":"https://images.unsplash.com/photo-1626814026160-2237a95fc5a0"
    },

    {
        "title":"Captain America: Civil War",
        "author":"Marvel Studios",
        "category":"Superhero",
        "image":"https://images.unsplash.com/photo-1507842217343-583bb7270b66"
    },

    {
        "title":"Iron Man",
        "author":"Marvel Comics",
        "category":"Superhero",
        "image":"https://images.unsplash.com/photo-1514329926535-7f6db2f4b2f4"
    },

    {
        "title":"Thor: Ragnarok",
        "author":"Marvel Studios",
        "category":"Superhero",
        "image":"https://images.unsplash.com/photo-1495446815901-a7297e633e8d"
    },

    {
        "title":"Doctor Strange",
        "author":"Marvel Studios",
        "category":"Superhero",
        "image":"https://images.unsplash.com/photo-1512820790803-83ca734da794"
    },

    {
        "title":"Black Panther",
        "author":"Marvel Studios",
        "category":"Superhero",
        "image":"https://images.unsplash.com/photo-1521587760476-6c12a4b040da"
    }

]

# ==========================================
# HERO SECTION
# ==========================================
st.markdown("""
<div class="hero">

<div class="hero-title">
Find Your Favorite Book
<br>
<span class="glow">Instantly</span>
</div>

<div class="hero-subtitle">
Search thousands of books with a fast and efficient system.
</div>

<div class="established-box">

<div class="established-title">
📚 SmartLib <span class="logo-blue">Archivio</span>
</div>

<div class="established-sub">
Established on 6 June 2022
</div>

</div>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# METRICS
# ==========================================
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-icon">📚</div>
        <div class="metric-title">Books Borrowed</div>
        <div class="metric-number">{len(st.session_state.cart)}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-icon">🛡</div>
        <div class="metric-title">Borrow Limit</div>
        <div class="metric-number glow">3</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-icon">🕒</div>
        <div class="metric-title">History</div>
        <div class="metric-number">{len(st.session_state.history)}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# SEARCH
# ==========================================
search = st.text_input(
    "🔎 Search your favorite books"
)

st.write("")

# ==========================================
# SEARCH LOGIC
# ==========================================
found = False

# ==========================================
# SEARCH BOOKS
# ==========================================
if search.strip() != "":

    for book in books:

        if search.lower().strip() in book["title"].lower():

            found = True

            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(
                    book["image"],
                    use_container_width=True
                )

            with col2:

                st.markdown(f"""
                <div class="book-card">

                <h1>{book["title"]}</h1>

                <p style="font-size:18px;color:#cbd5e1;">
                Author: {book["author"]}
                </p>

                <div class="tag">
                {book["category"]}
                </div>

                </div>
                """, unsafe_allow_html=True)

                # BORROW BUTTON
                if st.button(
                    f"Borrow {book['title']}",
                    key=book["title"]
                ):

                    if len(st.session_state.cart) < 3:

                        if book["title"] not in st.session_state.cart:

                            st.session_state.cart.append(
                                book["title"]
                            )

                            st.session_state.history.append(
                                f"📖 Borrowed: {book['title']}"
                            )

                            st.success(
                                "Book added successfully"
                            )

                            st.rerun()

                        else:
                            st.warning(
                                "Book already borrowed"
                            )

                    else:
                        st.error(
                            "Borrow limit reached"
                        )

    # BOOK NOT FOUND
    if not found:

        st.error(
            "❌ Book not found"
        )

# ==========================================
# BORROW CART
# ==========================================
st.write("")
st.write("")

st.markdown("""
<div class="section-title">
🛒 Borrow Cart
</div>
""", unsafe_allow_html=True)

if not st.session_state.cart:

    st.info("No books borrowed.")

else:

    for item in st.session_state.cart:

        col1, col2 = st.columns([5,1])

        with col1:
            st.success(f"✅ {item}")

        with col2:

            if st.button(
                "Return",
                key=f"return_{item}"
            ):

                st.session_state.cart.remove(item)

                st.session_state.history.append(
                    f"↩ Returned: {item}"
                )

                st.rerun()

# ==========================================
# HISTORY
# ==========================================
st.write("")
st.write("")

st.markdown("""
<div class="section-title">
🕒 History
</div>
""", unsafe_allow_html=True)

if not st.session_state.history:

    st.info("No borrowing history.")

else:

    for item in reversed(
        st.session_state.history
    ):

        st.markdown(f"""
        <div class="history-box">
        {item}
        </div>
        """, unsafe_allow_html=True)
