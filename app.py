import streamlit as st
import datetime
import calendar

st.title("Homework List")

# Initialize homework list
if "homework" not in st.session_state:
    st.session_state["homework"] = []

# Input new homework
hw = st.text_input("Homework")
date = st.date_input("Due Date", value=datetime.date.today())

# Add homework
if st.button("Add") and hw != "":
    st.session_state["homework"].append((hw, date))

# Show homework list
st.write("### Homework List")
for h, d in st.session_state["homework"]:
    st.write(f"{h} - {d.strftime('%d/%m/%Y')}")

# Select month and year
month = st.number_input("Month", min_value=1, max_value=12, value=datetime.date.today().month)
year = st.number_input("Year", min_value=2020, value=datetime.date.today().year)

# Generate calendar
cal = calendar.monthcalendar(year, month)
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

st.write("### Calendar")

# Header row
cols = st.columns(7)
for i, d in enumerate(days):
    cols[i].write(f"**{d}**")

# Rows for each week
for week in cal:
    cols = st.columns(7)
    for i, day in enumerate(week):
        if day == 0:
            cols[i].write(" ")  # empty cell
        else:
            day_date = datetime.date(year, month, day)
            tasks = [h for h, d in st.session_state["homework"] if d == day_date]
            text = f"{day}\n" + "\n".join(tasks) if tasks else str(day)
            cols[i].write(text)
    st.markdown("---")  # line between weeks
