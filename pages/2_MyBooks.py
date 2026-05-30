
import streamlit as st

# ==========================================
# SESSION STATE
# ==========================================

if "cart" not in st.session_state:
    st.session_state.cart = []

if "history" not in st.session_state:
    st.session_state.history = []

# ==========================================
# PAGE TITLE
# ==========================================

st.title("📖 My Books")

st.markdown("""
Manage your borrowed books here.
""")

# ==========================================
# EMPTY STATE
# ==========================================

if len(st.session_state.cart) == 0:

    st.info("No books borrowed yet.")

# ==========================================
# BOOK LIST
# ==========================================

else:

    st.subheader("📚 Borrowed Books")

    for book in st.session_state.cart[:]:

        with st.container(border=True):

            col1, col2 = st.columns([4,1])

            with col1:

                st.markdown(f"### {book}")

                st.caption("Borrowed successfully")

            with col2:

                st.markdown("<br>", unsafe_allow_html=True)

                if st.button(
                    "Return",
                    key=f"return_{book}",
                    use_container_width=True
                ):

                    st.session_state.cart.remove(book)

                    st.success(f"{book} returned!")

                    st.rerun()

# ==========================================
# CHECKOUT
# ==========================================

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "✅ Checkout All Books",
        use_container_width=True
    ):

        st.session_state.history.extend(
            st.session_state.cart
        )

        st.session_state.cart.clear()

        st.success("Checkout completed successfully!")

        st.rerun()
