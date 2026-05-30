import streamlit as st

if "cart" not in st.session_state:
    st.session_state.cart = []

if "history" not in st.session_state:
    st.session_state.history = []

st.title("📖 My Books")

if not st.session_state.cart:
    st.info("No books borrowed.")
else:
    for book in st.session_state.cart[:]:
        col1,col2 = st.columns([4,1])

        with col1:
            st.write(book)

        with col2:
            if st.button("Return", key=book):
                st.session_state.cart.remove(book)
                st.rerun()

    if st.button("Checkout"):
        st.session_state.history.extend(st.session_state.cart)
        st.session_state.cart.clear()
        st.success("Checkout complete")
