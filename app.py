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

st.header("Calendar")
month = st.selectbox("Month", range(1, 13), index=datetime.date.today().month-1)
year = st.number_input("Year", value=datetime.date.today().year, min_value=2020)
cal = calendar.monthcalendar(year, month)
for week in cal:
    st.write(" | ".join(["💀" if any(h[1].day == d and h[1].month == month for h in st.session_state["list"]) else str(d) if d else "" for d in week]))
    
for i, (task, due, subj) in enumerate(st.session_state["list"]):
    line = f"{task} ({subj}) - {due.strftime('%b %d')}"
    if due < today:
        line = "🔴 " + line
    st.markdown(f"<span style='color:{colors[subj]}'>{line}</span>", unsafe_allow_html=True)
    if st.button("Delete", key=i):
        st.session_state["list"].pop(i)
