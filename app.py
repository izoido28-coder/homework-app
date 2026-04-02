import streamlit as st
import datetime

st.title("Homework List")

# Initialize list
if "list" not in st.session_state:
    st.session_state["list"] = []

# Input fields
hw = st.text_input("Homework")
subject = st.selectbox("Subject", ["Math", "Science", "English", "History", "Other"])
date = st.date_input("Date", value=datetime.date.today())

# Add homework
if st.button("Add") and hw:
    st.session_state["list"].append((hw, date, subject))
    # Clear text input by using session state
    st.session_state["hw_input"] = ""

# Display homework
colors = {"Math":"blue","Science":"green","English":"orange","History":"purple","Other":"gray"}
today = datetime.date.today()

for i, (task, due, subj) in enumerate(st.session_state["list"]):
    line = f"{task} ({subj}) - {due.strftime('%b %d')}"
    if due < today:
        line = "🔴 " + line
    st.markdown(f"<span style='color:{colors[subj]}'>{line}</span>", unsafe_allow_html=True)
    if st.button("Delete", key=i):
        st.session_state["list"].pop(i)