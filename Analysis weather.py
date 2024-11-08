temperature = int(input("Введите температуру воздуха: "))
humidity = int(input("Введите влажность воздуха: "))
wind_speed = int(input("Введите скорость ветра: "))
is_raining = bool(input("Присутствует дождь? (Если нет оставьте поле пустым): "))

if temperature < 5 and wind_speed > 8:
    print("На улице суровая погода.")
if humidity < 30 and temperature > 30:
    print("На улице сухая и жаркая погода.")
if temperature > 25:
    print("На улице жаркая температура воздуха")
if temperature < 10:
    print("На улице холодная температура воздуха")
if humidity > 80:
    print("Высокая влажность.")
if wind_speed > 10:
    print("На улице сильный ветер")
if is_raining == True:
    print("Возьмите зонт.")
