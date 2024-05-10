import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from streamlit_echarts import st_echarts

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


st.sidebar.header("Выберите страну")
kaz_button = st.sidebar.button('Казахстан')
uzb_button = st.sidebar.button('Узбекистан')
tjk_button = st.sidebar.button('Таджикистан')
kgz_button = st.sidebar.button('Кыргызстан')
all_countries_button = st.sidebar.button('Общий график')
st.sidebar.header("Выберите тип графика")
line_chart_button = st.sidebar.button('Линейный график')
bar_chart_button = st.sidebar.button('Гистограмма')

F_ad_Prob_Mod_Sev_kaz_values = [0.0737473506983265, 0.044529239425859325, 0.07208697980276833, 0.09025550050680399]
F_ad_Prob_Mod_Sev_uzb_values = [0.09872602667454446, 0.12482079148104783, 0.1033934827101725, 0.16342414956949367]
F_ad_Prob_Mod_Sev_tjk_values = [0.13234311608076732, 0.11086727498562164, 0.19598527440470287, 0.23921461895440915]
F_ad_Prob_Mod_Sev_kgz_values = [0.1875365079274166, 0.21059007745097164, 0.19581301002148638, 0.19449654750600165]
years = [2014, 2015, 2016, 2017]


def plot_country_graph(country, values, years):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, values, marker='o', linestyle='-')
    ax.set_title(country)
    ax.set_xticks(years)
    ax.set_yticks(np.arange(0, 0.31, 0.05))
    ax.grid(True)
    st.pyplot(fig)


if kaz_button:
    plot_country_graph('Казахстан', F_ad_Prob_Mod_Sev_kaz_values, years)

elif uzb_button:
    plot_country_graph('Узбекистан', F_ad_Prob_Mod_Sev_uzb_values, years)

elif tjk_button:
    plot_country_graph('Таджикистан', F_ad_Prob_Mod_Sev_tjk_values, years)

elif kgz_button:
    plot_country_graph('Кыргызстан', F_ad_Prob_Mod_Sev_kgz_values, years)

elif all_countries_button:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, F_ad_Prob_Mod_Sev_kaz_values, marker='o', linestyle='-', label='Казахстан')
    ax.plot(years, F_ad_Prob_Mod_Sev_uzb_values, marker='o', linestyle='-', label='Узбекистан')
    ax.plot(years, F_ad_Prob_Mod_Sev_kgz_values, marker='o', linestyle='-', label='Кыргызстан')
    ax.plot(years, F_ad_Prob_Mod_Sev_tjk_values, marker='o', linestyle='-', label='Таджикистан')
    ax.set_title('Центральная Азия')
    ax.set_xticks(years)
    ax.set_yticks(np.arange(0, 0.3, 0.05))
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

if bar_chart_button:
    options = {
        "xAxis": {"type": "category", "data": ["2014", "2015", "2016", "2017"]},
        "yAxis": {"type": "value"},
        "series": [
            {"name": "Казахстан", "data": F_ad_Prob_Mod_Sev_kaz_values, "type": "bar"},
            {"name": "Узбекистан", "data": F_ad_Prob_Mod_Sev_uzb_values, "type": "bar"},
            {"name": "Таджикистан", "data": F_ad_Prob_Mod_Sev_tjk_values, "type": "bar"},
            {"name": "Кыргызстан", "data": F_ad_Prob_Mod_Sev_kgz_values, "type": "bar"}
        ],
    }
    st_echarts(options=options, height="400px")