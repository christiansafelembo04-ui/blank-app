import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="SmartLib Archivio",
    page_icon="📚",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================
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

/* Hide Streamlit default menu */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container {
    padding-top: 2rem;
    max-width: 95%;
}

/* HERO SECTION */
.hero {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    border-radius: 28px;
    padding: 40px;
    margin-bottom: 30px;
}

/* TITLES */
.hero-title {
    font-size: 55px;
    font-weight: 700;
    line-height: 1.1;
    color: white;
}

.hero-title span {
    color: #22d3ee;
}

.hero-sub {
    color: #cbd5e1;
    margin-top: 15px;
    font-size: 18px;
}

/* CARDS */
.card {
    background: rgba(15,23,42,0.75);
    border: 1px solid #334155;
    border-radius: 24px;
    padding: 20px;
    margin-bottom: 20px;
}

.sidebar-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 25px;
    margin-bottom: 20px;
}

/* BOOK */
.book-title {
    font-size: 28px;
    font-weight: 600;
    color: white;
}

.book-author {
    color: #94a3b8;
    margin-bottom: 10px;
}

.badge {
    display: inline-block;
    background: rgba(168,85,247,0.2);
    color: #c084fc;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 13px;
    margin-bottom: 12px;
}

.available {
    color: #22c55e;
    font-weight: 600;
}

/* LIMIT BOX */
.limit-box {
    background: linear-gradient(135deg, #2563eb, #4f46e5);
    border-radius: 24px;
    padding: 30px;
    text-align: center;
    color: white;
    margin-top: 20px;
}

/* BUTTON */
.stButton > button {
    background: linear-gradient(135deg, #22d3ee, #2563eb);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 20px;
    font-weight: 600;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #38bdf8, #3b82f6);
    color: white;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #64748b;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# DATABASE
# =====================================
books = [
    {
        "title": "Python Dasar",
        "author": "Archivio Team",
        "category": "Programming",
        "description": "Belajar Python dari dasar hingga mahir."
    },
    {
        "title": "AI Modern",
        "author": "Tech Publisher",
        "category": "Artificial Intelligence",
        "description": "Panduan memahami AI modern dan implementasi nyata."
    },
    {
        "title": "Data Science 101",
        "author": "Smart Academy",
        "category": "Data Science",
        "description": "Belajar analisis data dan machine learning."
    }
]

# =====================================
# SESSION STATE
# =====================================
if "cart" not in st.session_state:
    st.session_state.cart = []

# =====================================
# HEADER
# =====================================
st.markdown("""
<h1 style='font-size:42px; margin-bottom:30px; color:white;'>
📚 SmartLib <span style='color:#22d3ee;'>Archivio</span>
</h1>
""", unsafe_allow_html=True)

# =====================================
# HERO + STATUS
# =====================================
left, right = st.columns([3,1])

with left:

    st.markdown("""
    <div class='hero'>
        <div class='hero-title'>
            Find Your Favorite Book <span>Instantly</span>
        </div>

        
            Search thousands of books with a fast and efficient system.
        
    </div>
    """, unsafe_allow_html=True)

    search = st.text_input(
        "",
        placeholder="🔍 Search books, author, or category..."
    )

with right:

    st.markdown("<div class='sidebar-card'>", unsafe_allow_html=True)

    st.markdown("## 📘 Books Borrowed")

    st.markdown(
        f"<h1 style='font-size:55px; color:#22d3ee;'>{len(st.session_state.cart)} / 3</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style='color:white;'>
        You can borrow 
        <span style='color:#22d3ee; font-weight:bold;'>
        {3-len(st.session_state.cart)}
        </span> more book
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# FILTER BOOKS
# =====================================
filtered_books = []

for book in books:

    if (
        search.lower() in book["title"].lower()
        or search.lower() in book["author"].lower()
        or search.lower() in book["category"].lower()
    ):
        filtered_books.append(book)

# =====================================
# MAIN CONTENT
# =====================================
left_col, right_col = st.columns([2.2,1])

# =====================================
# BOOK LIST
# =====================================
with left_col:

    st.markdown(
        "<h2 style='color:white;'>📚 Available Books</h2>",
        unsafe_allow_html=True
    )

    for book in filtered_books:

        st.markdown(f"""
        <div class='card'>

            
            {book['title']}
            

            
            {book['author']}
            

            
            {book['category']}
            


            {book['description']}
            

            
            ● Available
        

        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Borrow {book['title']}"):

            if len(st.session_state.cart) >= 3:
                st.error("Borrow limit reached!")
                break

            if book["title"] not in st.session_state.cart:
                st.session_state.cart.append(book["title"])
                st.success(f"{book['title']} added to cart!")

# =====================================
# BORROW CART
# =====================================
with right_col:

    st.markdown("<div class='sidebar-card'>", unsafe_allow_html=True)

    st.markdown("## 🛒 Borrow Cart")

    if len(st.session_state.cart) == 0:
        st.write("No books borrowed yet.")

    else:

        for item in st.session_state.cart:

            st.markdown(f"""
            <div class='card'>
                <h3 style='color:white;'>{item}</h3>

                
                ● Ready to borrow
                
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class='limit-box'>
        <h3>Borrow Limit</h3>

        
        3 Books
        

        
        Maximum 3 books per session
        
    </div>
    """, unsafe_allow_html=True)

    st.button("Checkout", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# FOOTER
# =====================================
st.markdown("""
<div class='footer'>
SmartLib Archivio © 2026 | All rights reserved
</div>
""", unsafe_allow_html=True)
