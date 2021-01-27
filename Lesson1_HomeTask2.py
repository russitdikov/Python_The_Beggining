# 2.	Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

user_time_sec = int(input('Введите время в секундах: '))

time_hour = user_time_sec // 3600

if time_hour // 10 == 0:
    time_hour = f'{0}{time_hour}'

time_min = (user_time_sec % 3600) // 60

if time_min // 10 == 0:
    time_min = f'{0}{time_min}'
time_sec = (user_time_sec % 3600) % 60

if time_sec // 10 == 0:
    time_min = f'{0}{time_sec}'

print(f'{time_hour}:{time_min}:{time_sec}')
