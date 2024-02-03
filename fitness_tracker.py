import datetime as dt
FORMAT = '%H:%M:%S'
storage_data = {}
steps_km = 0.7
weight = 70
height = 176


def check_correct_data(data):
    if len(data) != 2 or data[0] is None or data[1] is None:
        return False
    return True


def check_correct_time(time):
    for time_check in storage_data.keys():
        cor_time = dt.datetime.strptime(time_check, FORMAT).time()
        if cor_time >= time and storage_data != {}:
            return False
    return True


def get_step_day(steps):
    for steps_check in storage_data.values():
        steps += steps_check
    return steps


def get_distance(steps):
    distance = round(steps_km * steps / 1000, 2)
    return distance


def get_spent_calories(distance, corr_time):
    hours = corr_time.hour + corr_time.minute/60
    spent_calories = round((0.035*weight + (distance / hours)**2/height * 0.029 * weight) * hours*60, 2)
    return spent_calories


def get_achievement(distance):
    if distance >= 6.5:
        achievement = 'Отличный результат! Цель достигнута.'
    elif distance >= 3.9:
        achievement = 'Неплохо! День был продуктивным.'
    elif distance >= 2:
        achievement = 'Маловато, но завтра наверстаем!'
    else:
        achievement = 'Лежать тоже полезно. Главное - участие, а не победа!'
    return achievement


def show_message(time, days_steps, dist, calories, achievement):
    print(f'''
Время: {time}.
Количество шагов за сегодня: {days_steps}.
Дистанция составила {dist}.
Вы сожгли {calories} ккал.
{achievement}
''')


def accept_package(data):
    if check_correct_data(data) is False:
        return 'Некорректный пакет данных'
    time, steps = data
    corr_time = dt.datetime.strptime(time, FORMAT).time()
    if check_correct_time(corr_time) is False:
        return 'Некорректное значение времени'
    days_steps = get_step_day(steps)
    dist = get_distance(steps)
    calories = get_spent_calories(dist, corr_time)
    achiev = get_achievement(dist)
    print(show_message(time, days_steps, dist, calories, achiev))
    storage_data[time] = steps
    return storage_data


pack_1 = ('09:36:25', 4596)
pack_2 = ('11:52:25', 3500)
pack_3 = ('18:06:25', 7800)

accept_package(pack_1)
accept_package(pack_2)
accept_package(pack_3)
