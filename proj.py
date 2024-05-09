import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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
data_uzb3 = pd.read_excel('uzb_2017xlsx')



df_kgz_2014 = pd.read_excel('kgz_2014.xlsx')
df_kgz_2014.fillna(0)
df_kgz_2014.to_excel('kgz_2014.xlsx', index=False)

df_kgz_2015 = pd.read_excel('kgz_2015.xlsx')
df_kgz_2015.fillna(0)
df_kgz_2015.to_excel('kgz_2015.xlsx', index=False)

df_kgz_2016 = pd.read_excel('kgz_2016.xlsx')
df_kgz_2016.fillna(0)
df_kgz_2016.to_excel('kgz_2016.xlsx', index=False)

df_kgz_2017 = pd.read_excel('kgz_2017.xlsx')
df_kgz_2017.fillna(0)
df_kgz_2017.to_excel('kgz_2017.xlsx', index=False)

df_kz_2014 = pd.read_excel('kz_2014.xlsx')
df_kz_2014.fillna(0)
df_kz_2014.to_excel('kz_2014.xlsx', index=False)

df_kz_2015 = pd.read_excel('kz_2015.xlsx')
df_kz_2015.fillna(0)
df_kz_2015.to_excel('kz_2015.xlsx', index=False)

df_kz_2016 = pd.read_excel('kz_2016.xlsx')
df_kz_2016.fillna(0)
df_kz_2016.to_excel('kz_2016.xlsx', index=False)

df_kz_2017 = pd.read_excel('kz_2017.xlsx')
df_kz_2017.fillna(0)
df_kz_2017.to_excel('kz_2017.xlsx', index=False)

df_tjk_2014 = pd.read_excel('tjk_2014.xlsx')
df_tjk_2014.fillna(0)
df_tjk_2014.to_excel('tjk_2014.xlsx', index=False)

df_tjk_2015 = pd.read_excel('tjk_2015.xlsx')
df_tjk_2015.fillna(0)
df_tjk_2015.to_excel('tjk_2015.xlsx', index=False)

df_tjk_2016 = pd.read_excel('tjk_2016.xlsx')
df_tjk_2016.fillna(0)
df_tjk_2016.to_excel('tjk_2016.xlsx', index=False)

df_tjk_2017 = pd.read_excel('tjk_2017.xlsx')
df_tjk_2017.fillna(0)
df_tjk_2017.to_excel('tjk_2017.xlsx', index=False)

df_uzb_2014 = pd.read_excel('uzb_2014.xlsx')
df_uzb_2014.fillna(0)
df_uzb_2014.to_excel('uzb_2014.xlsx', index=False)

df_uzb_2015 = pd.read_excel('uzb_2015.xlsx')
df_uzb_2015.fillna(0)
df_uzb_2015.to_excel('uzb_2015.xlsx', index=False)

df_uzb_2016 = pd.read_excel('uzb_2016.xlsx')
df_uzb_2016.fillna(0)
df_uzb_2016.to_excel('uzb_2016.xlsx', index=False)

df_uzb_2017 = pd.read_excel('uzb_2017.xlsx')
df_uzb_2017.fillna(0)
df_uzb_2017.to_excel('uzb_2017.xlsx', index=False)

mod_sev_kgz_2014 = (df_kgz_2014['Prob_Mod_Sev'] * df_kgz_2014['wt']).sum() / df_kgz_2014['wt'].sum()

mod_sev_kgz_2015 = (df_kgz_2015['Prob_Mod_Sev'] * df_kgz_2015['wt']).sum() / df_kgz_2015['wt'].sum()

mod_sev_kgz_2016 = (df_kgz_2016['Prob_Mod_Sev'] * df_kgz_2016['wt']).sum() / df_kgz_2016['wt'].sum()

mod_sev_kgz_2017 = (df_kgz_2017['Prob_Mod_Sev'] * df_kgz_2017['wt']).sum() / df_kgz_2017['wt'].sum()

mod_sev_kz_2014 = (df_kz_2014['Prob_Mod_Sev'] * df_kz_2014['wt']).sum() / df_kz_2014['wt'].sum()

mod_sev_kz_2015 = (df_kz_2015['Prob_Mod_Sev'] * df_kz_2015['wt']).sum() / df_kz_2015['wt'].sum()

mod_sev_kz_2016 = (df_kz_2016['Prob_Mod_Sev'] * df_kz_2016['wt']).sum() / df_kz_2016['wt'].sum()

mod_sev_kz_2017 = (df_kz_2017['Prob_Mod_Sev'] * df_kz_2017['wt']).sum() / df_kz_2017['wt'].sum()

mod_sev_tjk_2014 = (df_tjk_2014['Prob_Mod_Sev'] * df_tjk_2014['wt']).sum() / df_tjk_2014['wt'].sum()

mod_sev_tjk_2015 = (df_tjk_2015['Prob_Mod_Sev'] * df_tjk_2015['wt']).sum() / df_tjk_2015['wt'].sum()

mod_sev_tjk_2016 = (df_tjk_2016['Prob_Mod_Sev'] * df_tjk_2016['wt']).sum() / df_tjk_2016['wt'].sum()

mod_sev_tjk_2017 = (df_tjk_2017['Prob_Mod_Sev'] * df_tjk_2017['wt']).sum() / df_tjk_2017['wt'].sum()

mod_sev_uzb_2014 = (df_uzb_2014['Prob_Mod_Sev'] * df_uzb_2014['wt']).sum() / df_uzb_2014['wt'].sum()

mod_sev_uzb_2015 = (df_uzb_2015['Prob_Mod_Sev'] * df_uzb_2015['wt']).sum() / df_uzb_2015['wt'].sum()

mod_sev_uzb_2016 = (df_uzb_2016['Prob_Mod_Sev'] * df_uzb_2016['wt']).sum() / df_uzb_2016['wt'].sum()

mod_sev_uzb_2017 = (df_uzb_2017['Prob_Mod_Sev'] * df_uzb_2017['wt']).sum() / df_uzb_2017['wt'].sum()

kgz_values = [mod_sev_kgz_2014, mod_sev_kgz_2015, mod_sev_kgz_2016, mod_sev_kgz_2017]

kz_values = [mod_sev_kz_2014, mod_sev_kz_2015, mod_sev_kz_2016, mod_sev_kz_2017]

tjk_values = [mod_sev_tjk_2014, mod_sev_tjk_2015, mod_sev_tjk_2016, mod_sev_tjk_2017]

uzb_values = [mod_sev_uzb_2014, mod_sev_uzb_2015, mod_sev_uzb_2016, mod_sev_uzb_2017]



#years = range(2014, 2018)

#plt.figure(figsize=(10, 6))
#plt.plot(years, kgz_values, marker='o', linestyle='-', label='Казахстан')
#plt.plot(years, kz_values, marker='o', linestyle='-', label='Узбекистан')
#plt.plot(years, uzb_values, marker='o', linestyle='-', label='Кыргызстан')
#plt.plot(years, tjk_values, marker='o', linestyle='-', label='Таджикистан')
#plt.title('Центральная Азия')
#plt.xticks(years)
#plt.yticks(np.arange(0, 0.3, 0.05))
#plt.legend()
#plt.grid(True)
#plt.show()