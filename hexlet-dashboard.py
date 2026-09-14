# prepare_data.py
import pandas as pd
import numpy as np

# 1. Загрузка исходных срезов
df_exp = pd.read_excel('2026-08-27 Твой опыт в Хекслет Колледже (1).xlsx')
df_cur = pd.read_excel('2026-08-27 Анкета оценки кураторов (1).xlsx')
df_tea = pd.read_excel('2026-08-27 Студенческая оценка преподавателя (1).xlsx')

# 2. Нормализация городов
def clean_city(col):
    return col.astype(str).str.strip()

# 3. Расчет NPS: Промоутеры (9-10), Нейтралы (7-8), Критики (0-6)
# Формула NPS = (% Промоутеров - % Критиков) * 100
def calc_nps_category(score):
    if pd.isna(score):
        return np.nan
    score = float(score)
    if score >= 9:
        return 'Сторонник'
    elif score >= 7:
        return 'Нейтрал'
    else:
        return 'Критик'

# 4. Сохранение агрегированных витрин для дашборда
# (Пример сохранения очищенных файлов в репозиторий)
# df_cur.to_csv('data/curators_eval.csv', index=False, encoding='utf-8-sig')
# df_tea.to_csv('data/teachers_eval.csv', index=False, encoding='utf-8-sig')