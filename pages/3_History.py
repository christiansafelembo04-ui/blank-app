
import streamlit as st

# ==========================================
# SESSION STATE
# ==========================================

if "history" not in st.session_state:
    st.session_state.history = []

# ==========================================
# PAGE TITLE
# ==========================================

st.title("🕒 Borrow History")

st.markdown("""
View all books that have been checked out.
""")

# ==========================================
# EMPTY STATE
# ==========================================

if len(st.session_state.history) == 0:

    st.info("No borrowing history yet.")

# ==========================================
# HISTORY LIST
# ==========================================

else:

    st.subheader("📚 Borrow Records")

    for index, item in enumerate(
        st.session_state.history,
        start=1
    ):

        with st.container(border=True):

            col1, col2 = st.columns([5,1])

            with col1:

                st.markdown(f"### {item}")

                st.caption("Returned / Checked Out")

            with col2:

                st.metric(
                    "Record",
                    f"#{index}"
                )

# ==========================================
# TOTAL
# ==========================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.success(
        f"Total history records: {len(st.session_state.history)}"
    )


