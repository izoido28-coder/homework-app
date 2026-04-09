import streamlit as st
import datetime
import calendar

st.title("Lista de Tareas - Básico")

# Inicializar lista de tareas
if "tareas" not in st.session_state:
    st.session_state["tareas"] = []

# Ingresar nueva tarea
tarea = st.text_input("Tarea")
fecha = st.date_input("Fecha", value=datetime.date.today())

# Botón para agregar tarea
if st.button("Agregar") and tarea != "":
    st.session_state["tareas"].append((tarea, fecha))

# Mostrar lista de tareas
st.write("### Lista de Tareas")
for t, f in st.session_state["tareas"]:
    st.write(f"{t} - {f.strftime('%d/%m/%Y')}")

# Selección de mes y año
mes = st.number_input("Mes", min_value=1, max_value=12, value=datetime.date.today().month)
año = st.number_input("Año", min_value=2020, value=datetime.date.today().year)

# Generar calendario
cal = calendar.monthcalendar(año, mes)
dias = ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"]

st.write("### Calendario")
# Cabecera
cols = st.columns(7)
for i, d in enumerate(dias):
    cols[i].write(f"**{d}**")

# Filas del calendario
for semana in cal:
    cols = st.columns(7)
    for i, dia in enumerate(semana):
        if dia == 0:
            cols[i].write(" ")
        else:
            dia_date = datetime.date(año, mes, dia)
            tareas_dia = [t for t, f in st.session_state["tareas"] if f == dia_date]
            if tareas_dia:
                texto = f"{dia}\n" + "\n".join(tareas_dia)
            else:
                texto = str(dia)
            cols[i].write(texto)
