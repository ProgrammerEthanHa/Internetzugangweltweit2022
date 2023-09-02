import streamlit as st
import pandas as pd
import altair as alt

st.header("Mehr als Drittel der Weltbevölkerung ist offline")
st.subheader("Internetzugang weltweit 2022")

source = pd.DataFrame({
        'Anteil(%)': [34, 66],
        'Zugang': ['ohne Zugang', 'mit Zugang']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Zugang:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    2023
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Schätzung ITU")