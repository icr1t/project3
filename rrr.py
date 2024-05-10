import pandas as pd
import streamlit as st
import altair as alt

# Данные для графика
data = pd.DataFrame({
    'Year': [2014, 2015, 2016, 2017],
    'Probability': [0.0737, 0.0445, 0.0721, 0.0903],
})

# Создание графика с помощью Altair
chart = alt.Chart(data).mark_line().encode(
    x='Year',
    y='Probability'
).properties(
    width=500,
    height=300,
    title='Probability of Moderate Severity'
)

# Отображение графика с помощью st.altair_chart
st.altair_chart(chart)
