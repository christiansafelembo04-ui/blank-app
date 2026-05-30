
import streamlit as st

# ==========================================
# PAGE TITLE
# ==========================================

st.title("ℹ️ About SmartLib Archivio")

# ==========================================
# HERO CARD
# ==========================================

st.markdown("""
<div style="
    background: rgba(255,255,255,0.05);
    padding: 35px;
    border-radius: 25px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-top: 20px;
">

<h1 style="
    color:white;
    margin-bottom:10px;
">
📚 SmartLib Archivio
</h1>

<p style="
    color:#cbd5e1;
    font-size:18px;
    line-height:1.8;
">

SmartLib Archivio is a modern digital library platform
designed to help users discover, borrow,
and manage books efficiently through
a clean and user-friendly experience.

</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# INFORMATION
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:

    st.markdown("""
    <div style="
        background: rgba(255,255,255,0.05);
        padding:25px;
        border-radius:20px;
        border:1px solid rgba(255,255,255,0.08);
    ">

    <h3 style="color:white;">
    📅 Established
    </h3>

    <p style="
        color:#cbd5e1;
        font-size:18px;
    ">
    June 4, 2020
    </p>

    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div style="
        background: rgba(255,255,255,0.05);
        padding:25px;
        border-radius:20px;
        border:1px solid rgba(255,255,255,0.08);
    ">

    <h3 style="color:white;">
    🚀 Focus
    </h3>

    <p style="
        color:#cbd5e1;
        font-size:18px;
    ">
    Modern UI, efficient borrowing,
    and easy digital access.
    </p>

    </div>
    """, unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

st.success(
    "SmartLib Archivio © 2026 | Digital Library Platform"
)

