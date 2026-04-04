import streamlit as st
import datetime
import calendar

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

month = st.selectbox("Month", range(1, 13), index=datetime.date.today().month - 1)
year = st.number_input("Year", value=datetime.date.today().year, min_value=2020)

cal = calendar.monthcalendar(year, month)
st.write(" | ".join(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]))

for week in cal:
    row = []
    for d in week:
        if d == 0:
            row.append("")
        else:
            day_date = datetime.date(year, month, d)
            hws = [f"{hw}({subj})" for hw, due, subj in st.session_state["list"] if due == day_date]
            row.append(f"{d}<br><small>{'; '.join(hws[:2])}</small>" if hws else str(d))
    st.markdown(" | ".join(row), unsafe_allow_html=True)
