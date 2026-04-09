import streamlit as st
import datetime
import calendar

st.title("Homework List - Basic")

# Initialize homework list
if "homework" not in st.session_state:
    st.session_state["homework"] = []

# Input for new homework
new_hw = st.text_input("Enter Homework")
due_date = st.date_input("Due Date", value=datetime.date.today())

# Button to add homework
if st.button("Add") and new_hw != "":
    st.session_state["homework"].append((new_hw, due_date))

import streamlit as st
import datetime
import calendar

st.title("Homework List - Basic with Delete")

# Initialize homework list
if "homework" not in st.session_state:
    st.session_state["homework"] = []

# Input for new homework
new_hw = st.text_input("Enter Homework")
due_date = st.date_input("Due Date", value=datetime.date.today())

# Button to add homework
if st.button("Add") and new_hw != "":
    st.session_state["homework"].append((new_hw, due_date))

# Display homework list with delete buttons
st.write("### Homework List")
for i, (hw, d) in enumerate(st.session_state["homework"]):
    col1, col2 = st.columns([4, 1])
    col1.write(f"{hw} - {d.strftime('%d/%m/%Y')}")
    if col2.button("Delete", key=f"del_{i}"):
        st.session_state["homework"].pop(i)
        st.experimental_rerun()  # refresh app to update list

# Select month and year
month = st.number_input("Month", min_value=1, max_value=12, value=datetime.date.today().month)
year = st.number_input("Year", min_value=2020, value=datetime.date.today().year)

# Generate calendar
cal = calendar.monthcalendar(year, month)
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

st.write("### Calendar")

# Calendar header
cols = st.columns(7)
for i, day in enumerate(days):
    cols[i].write(f"**{day}**")

# Calendar rows
for week in cal:
    cols = st.columns(7)
    for i, day in enumerate(week):
        if day == 0:
            cols[i].write(" ")  # empty cell
        else:
            day_date = datetime.date(year, month, day)
            tasks = [hw for hw, d in st.session_state["homework"] if d == day_date]
            cell_text = f"{day}\n" + "\n".join(tasks) if tasks else str(day)
            cols[i].write(cell_text)
    st.markdown("---")  # line between weeks
# Generate calendar
cal = calendar.monthcalendar(year, month)
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

st.write("### Calendar")

# Calendar header
cols = st.columns(7)
for i, day in enumerate(days):
    cols[i].write(f"**{day}**")

# Calendar rows
for week in cal:
    cols = st.columns(7)
    for i, day in enumerate(week):
        if day == 0:
            cols[i].write(" ")  # empty cell
        else:
            day_date = datetime.date(year, month, day)
            tasks = [hw for hw, d in st.session_state["homework"] if d == day_date]
            cell_text = f"{day}\n" + "\n".join(tasks) if tasks else str(day)
            cols[i].write(cell_text)
    st.markdown("---")  # line between weeks
