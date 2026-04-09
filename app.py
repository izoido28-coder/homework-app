import streamlit as st
import datetime
import calendar

st.title("Homework List")

# Initialize homework list
if "homework" not in st.session_state:
    st.session_state["homework"] = []

# Input for new homework
new_hw = st.text_input("Enter Homework", key="hw_input")
due_date = st.date_input("Due Date", value=datetime.date.today(), key="date_input")

# Button to add homework
if st.button("Add", key="add_button") and new_hw != "":
    st.session_state["homework"].append((new_hw, due_date))

# Safe delete: store index to remove
delete_index = None

# Display homework list with delete buttons
st.write("### Homework List")
for i, (hw, d) in enumerate(st.session_state["homework"]):
    col1, col2 = st.columns([4, 1])
    col1.write(f"{hw} - {d.strftime('%d/%m/%Y')}")
    if col2.button("Delete", key=f"del_{i}"):
        delete_index = i

# Remove the item outside of the loop
if delete_index is not None:
    st.session_state["homework"].pop(delete_index)

# Month and year selection
month = st.number_input("Month", min_value=1, max_value=12, value=datetime.date.today().month)
year = st.number_input("Year", min_value=2020, value=datetime.date.today().year)

# Generate calendar
cal = calendar.monthcalendar(year, month)
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
st.write("### Calendar")

# Calendar header
cols = st.columns(7)
for i, day in enumerate(days):
    col1.write(f"{hw}")
col1.write(f"{d.strftime('%d/%m/%Y')}")

# Calendar rows
for week in cal:
    cols = st.columns(7)
    for i, day in enumerate(week):
        if day == 0:
            cols[i].write(" ")
        else:
            day_date = datetime.date(year, month, day)
            tasks = [hw for hw, d in st.session_state["homework"] if d == day_date]
            cell_text = f"{day}"
            if tasks:
                cell_text += "\n" + "\n".join(tasks)
            cols[i].write(cell_text)
    st.markdown("---")  # 
