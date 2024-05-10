import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Загружаем данные
data_kz = pd.read_excel('kz_2014.xlsx')
data_kz1 = pd.read_excel('kz_2015.xlsx')
data_kz2 = pd.read_excel('kz_2016.xlsx')
data_kz3 = pd.read_excel('kz_2017.xlsx')

data_kgz = pd.read_excel('kgz_2014.xlsx')
data_kgz1 = pd.read_excel('kgz_2015.xlsx')
data_kgz2 = pd.read_excel('kgz_2016.xlsx')
data_kgz3 = pd.read_excel('kgz_2017.xlsx')

data_tjk = pd.read_excel('tjk_2014.xlsx')
data_tjk1 = pd.read_excel('tjk_2015.xlsx')
data_tjk2 = pd.read_excel('tjk_2016.xlsx')
data_tjk3 = pd.read_excel('tjk_2017.xlsx')

data_uzb = pd.read_excel('uzb_2014.xlsx')
data_uzb1 = pd.read_excel('uzb_2015.xlsx')
data_uzb2 = pd.read_excel('uzb_2016.xlsx')
data_uzb3 = pd.read_excel('uzb_2017.xlsx')

# Определяем функции для построения графиков
def plot_kz():
    plt.plot(data_kz['Year'], data_kz['Prob_Mod_Sev'], label='Kazakhstan')
    plt.xlabel('Year')
    plt.ylabel('Probability')
    plt.title('Probability of Moderate Severity in Kazakhstan')
    plt.legend()
    st.pyplot()

def plot_kgz():
    plt.plot(data_kgz['Year'], data_kgz['Prob_Mod_Sev'], label='Kyrgyzstan')
    plt.xlabel('Year')
    plt.ylabel('Probability')
    plt.title('Probability of Moderate Severity in Kyrgyzstan')
    plt.legend()
    st.pyplot()

def plot_tjk():
    plt.plot(data_tjk['Year'], data_tjk['Prob_Mod_Sev'], label='Tajikistan')
    plt.xlabel('Year')
    plt.ylabel('Probability')
    plt.title('Probability of Moderate Severity in Tajikistan')
    plt.legend()
    st.pyplot()

def plot_uzb():
    plt.plot(data_uzb['Year'], data_uzb['Prob_Mod_Sev'], label='Uzbekistan')
    plt.xlabel('Year')
    plt.ylabel('Probability')
    plt.title('Probability of Moderate Severity in Uzbekistan')
    plt.legend()
    st.pyplot()

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
