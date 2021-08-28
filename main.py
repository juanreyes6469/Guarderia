import streamlit as st
from datetime import date
from pathlib import Path
import base64

def numOfDays(date1, date2):
    return (date2-date1).days

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

header = st.container()
insertion = st.container()

with header:
    st.title("Guardería de Mamás")
    header_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(img_to_bytes("header.png"))
    st.markdown(header_html, unsafe_allow_html=True,)

with insertion:
    st.header("LLena los campos:")

    sel_col,disp_col = st.columns(2)

    # day = sel_col.slider("Día de llegada: ", min_value=1,max_value=31,value=1,step=1)
    # mes = sel_col.slider("Mes de llegada: ", min_value=1,max_value=12,value=1,step=1)

    # day_1 = sel_col.slider("Día de salida: ", min_value=1,max_value=31,value=1,step=1)
    # mes_1 = sel_col.slider("Mes de salida: ", min_value=1,max_value=12,value=1,step=1)
    fecha_1 = sel_col.date_input('start date')
    fecha_2 = sel_col.date_input('end date')

    num_gatos= sel_col.slider("Número de gaticos: ", min_value=1,max_value=10,value=1,step=1)

    # ano,ano1=2021,2021

    rec = sel_col.selectbox("Recargo de Recogida: ", options=[0,5000,10000,15000,20000], index =0)

    # date1 = date(int(ano), int(mes), int(day))
    # date2 = date(int(ano1), int(mes_1), int(day_1))
    date1 = fecha_1
    date2 = fecha_2

    recargo_recogida = int(rec)

    ans = numOfDays(date1, date2)

    disp_col.subheader("El gato se quedó esta cantidad de noches: ")
    disp_col.write(ans)

    disp_col.subheader("Valor a cobrar en pesos: ")
    disp_col.write(15000*ans*int(num_gatos) + recargo_recogida)

    disp_col.subheader("Si se quedó hasta más de las 9:00 pm:")
    disp_col.write((15000)*(ans+1)*int(num_gatos) + recargo_recogida)