import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Загружаем данные
data_kz = pd.read_excel('./333/kz_2014.xlsx')
data_kz1 = pd.read_excel('./333/kz_2015.xlsx')
data_kz2 = pd.read_excel('./333/kz_2016.xlsx')
data_kz3 = pd.read_excel('./333/kz_2017.xlsx')

data_kgz = pd.read_excel('./333/kgz_2014.xlsx')
data_kgz1 = pd.read_excel('./333/kgz_2015.xlsx')
data_kgz2 = pd.read_excel('./333/kgz_2016.xlsx')
data_kgz3 = pd.read_excel('./333/kgz_2017.xlsx')

data_tjk = pd.read_excel('./333/tjk_2014.xlsx')
data_tjk1 = pd.read_excel('./333/tjk_2015.xlsx')
data_tjk2 = pd.read_excel('./333/tjk_2016.xlsx')
data_tjk3 = pd.read_excel('./333/tjk_2017.xlsx')

data_uzb = pd.read_excel('./333/uzb_2014.xlsx')
data_uzb1 = pd.read_excel('./333/uzb_2015.xlsx')
data_uzb2 = pd.read_excel('./333/uzb_2016.xlsx')
data_uzb3 = pd.read_excel('./333/uzb_2017.xlsx')

# Определяем функции для построения графиков
years = [2014, 2015, 2016, 2017]

def plot_country_graph(country, values, years):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, values, marker='o', linestyle='-')
    ax.set_title(country)
    ax.set_xticks(years)
    ax.set_yticks(np.arange(0, 0.31, 0.05))
    ax.grid(True)
    st.pyplot(fig)


# Создаем кнопки и связываем их с соответствующими функциями построения графиков
button_kz = st.button("Показать график для Kazakhstan")
button_kgz = st.button("Показать график для Kyrgyzstan")
button_tjk = st.button("Показать график для Tajikistan")
button_uzb = st.button("Показать график для Uzbekistan")

# Проверяем, была ли нажата какая-либо кнопка и вызываем соответствующую функцию
if button_kz:
    plot_kz()

if button_kgz:
    plot_kgz()

if button_tjk:
    plot_tjk()

if button_uzb:
    plot_uzb()
