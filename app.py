import streamlit as st

if "list" not in st.session_state:
    st.session_state["list"] = []

st.title("Homework List")

hw = st.text_input("Homework")
date = st.date_input("Date")

if st.button("Add"):
    st.session_state["list"].append((hw, date))

for i, item in enumerate(st.session_state["list"]):
    st.write(item)
    if st.button("Delete", key=i):
        st.session_state["list"].pop(i)
        st.rerun()