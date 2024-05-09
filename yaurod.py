import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Определение списка стран и годов
countries = ['kgz', 'kz', 'tjk', 'uzb']
years = range(2014, 2018)

# Создание пустых списков для хранения значений m для каждой страны
m_values = {country: [] for country in countries}

# Загрузка данных для каждой страны и каждого года
def load_data(country, year):
    @st.cache_data  # Используем st.cache_data вместо st.cache
    def _load_data(country, year):
        df = pd.read_excel(f'./333/{country}_{year}.xlsx')
        return df

    return _load_data(country, year)


# Вычисление значений m для каждой страны и года
def calculate_m_values():
    for country in countries:
        for year in years:
            # Загружаем данные
            df = load_data(country, year)
            # Заполняем пропущенные значения нулями
            df.fillna(0, inplace=True)
            # Вычисляем значение m
            m_value = (df['Prob_Mod_Sev'] * df['wt']).sum() / df['wt'].sum()
            # Добавляем значение m в соответствующий список
            m_values[country].append(m_value)

# Вызываем функцию для вычисления значений m
calculate_m_values()

# Создание графика для страны и года
def plot_data(country, year):
    st.subheader(f'График для {country} {year}')
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['blue', 'green', 'orange', 'red']  # Цвета для линий каждой страны
    markers = ['o', 's', 'D', '^']  # Маркеры для точек на графике
    for idx, (country_name, m_list) in enumerate(m_values.items()):
        ax.plot(years, m_list, marker=markers[idx], linestyle='-', color=colors[idx], label=country_name)
    ax.set_title(f'Среднее значение m для {country} {year}', fontsize=16)
    ax.set_xlabel('Год', fontsize=12)
    ax.set_ylabel('Среднее значение m', fontsize=12)
    ax.set_xticks(np.arange(2014, 2018, step=1))
    ax.grid(True)  # Добавляем сетку на график
    ax.legend(fontsize=12)  # Улучшаем легенду
    plt.tight_layout()  # Улучшаем расположение элементов на графике
    st.pyplot(fig)  # Передаем объект фигуры в st.pyplot

st.title('Анализ данных по странам Центральной Азии')
st.markdown('Это приложение анализирует данные по странам Центральной Азии.')

selected_country = st.selectbox('Выберите страну:', countries)
selected_year = st.selectbox('Выберите год:', years)

st.subheader(f'Данные для {selected_country} за {selected_year}')
df = load_data(selected_country, selected_year)
st.write(df)  # Показываем данные
plot_data(selected_country, selected_year)  # Строим график