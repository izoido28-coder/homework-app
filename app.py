import streamlit as st
import datetime
import calendar
import pandas as pd

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

# Display homework (replace your whole display section with this)
colors = {"Math":"blue","Science":"green","English":"orange","History":"purple","Other":"gray"}
today = datetime.date.today()

for i, (task, due, subj) in enumerate(st.session_state["list"]):
    line = f"{task} ({subj}) - {due.strftime('%b %d')}"
    if due < today:
        line = "🔴 " + line
    st.markdown(f"<span style='color:{colors[subj]}'>{line}</span>", unsafe_allow_html=True)
    if st.button("❌", key=f"d{i}"):
        st.session_state["list"].pop(i)
        st.rerun()
month = st.selectbox("Month", range(1, 13), index=datetime.date.today().month - 1)
year = st.number_input("Year", value=datetime.date.today().year, min_value=2020)

cal = calendar.monthcalendar(year, month)
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

cols = st.columns(7)
for i, d in enumerate(days):
    cols[i].markdown(f"**{d}**")

for week in cal:
    cols = st.columns(7)
    for i, day in enumerate(week):
        if day == 0:
            cols[i].markdown("")
        else:
            day_date = datetime.date(year, month, day)
            items = [f"- {hw} ({subj})" for hw, due, subj in st.session_state["list"] if due == day_date]
            box = f"**{day}**<br>" + "<br>".join(items) if items else f"**{day}**"
            cols[i].markdown(box, unsafe_allow_html=True)
