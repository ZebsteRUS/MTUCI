from pyowm import OWM

owm = OWM('1c918a32f2b9d695678d022868835456')
place = input("Введите название города ")
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather

# темература
t = w.temperature("celsius")
t1 = t['temp']
t2 = t['feels_like']
t3 = t['temp_max']
t4 = t['temp_min']
# доп. данные
v = w.wind()["speed"]
h = w.humidity
p = w.pressure['press']

print(f"В городе {place} темература {t1} \nощущается как {t2} \nмаксимальная темература {t3} \nминимальная температура {t4}"
      f" \nвлажность воздуха {h}% \nскорость ветра {v} м/с \nдавление {p} мм.рт.ст")
