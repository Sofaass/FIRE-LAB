import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1. Загрузка данных
daily = pd.read_csv("data/daily_weather_fires.csv")

daily["time"] = pd.to_datetime(daily["time"])
daily = daily.sort_values("time").reset_index(drop=True)

# 2. Создание признака предыдущего дня
daily["previous_day"] = daily["detections"].shift(1)

# Первый день исключаем, так как нет данных за предыдущий день
daily = daily.dropna(subset=["previous_day"]).copy()

# 3. Признаки и целевой показатель
features = [
    "temperature_2m_mean (°C)",
    "precipitation_sum (mm)",
    "wind_speed_10m_max (km/h)",
    "shortwave_radiation_sum (MJ/m²)",
    "previous_day"
]

X = daily[features]
y = daily["detections"]

# 4. Три последовательные проверки по времени
# В каждом эксперименте обучение идёт на более ранних днях
# Проверка — на следующих 15 днях
train_sizes = [40, 55, 70]
test_size = 15

results = []

for number, train_size in enumerate(train_sizes, start=1):

    X_train = X.iloc[:train_size]
    X_test = X.iloc[train_size:train_size + test_size]

    y_train = y.iloc[:train_size]
    y_test = y.iloc[train_size:train_size + test_size]

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Прогноз линейной регрессии
    ai_prediction = model.predict(X_test)
    ai_prediction = np.maximum(0, ai_prediction)

    # Базовый прогноз — значение предыдущего дня
    baseline_prediction = X_test["previous_day"].to_numpy()

    ai_mae = mean_absolute_error(y_test, ai_prediction)
    baseline_mae = mean_absolute_error(
        y_test,
        baseline_prediction
    )

    results.append({
        "Период": number,
        "Начало проверки": daily.iloc[train_size]["time"].date(),
        "Конец проверки": daily.iloc[
            train_size + test_size - 1
        ]["time"].date(),
        "MAE модели ИИ": round(ai_mae, 2),
        "MAE базового метода": round(baseline_mae, 2)
    })

# 5. Вывод результатов
results_df = pd.DataFrame(results)

print("\nРЕЗУЛЬТАТЫ ПРОВЕРКИ МОДЕЛИ\n")
print(results_df.to_string(index=False))

print("\nСредняя MAE модели ИИ:",
      round(results_df["MAE модели ИИ"].mean(), 2))

print("Средняя MAE базового метода:",
      round(results_df["MAE базового метода"].mean(), 2))
