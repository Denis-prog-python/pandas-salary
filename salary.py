import pandas as pd

# Загрузка данных (указываем кодировку для кириллических символов)
df = pd.read_csv('dz.csv', encoding='utf-8')

# Преобразование Salary в числовой формат и удаление строк с пропусками
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df = df.dropna(subset=['Salary'])

# Группировка по городам и расчет средней зарплаты
result = df.groupby('City')['Salary'].mean().round(2)

print("Средняя зарплата по городам:")
print(result)