# 3.	Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

user_month = int(input('Введите номер месяца от 1 до 12:'))

print('*'*10, 'С помощью словаря','*'*10 )
month_dict = {'1': 'зима(январь)', '2': 'зима(февраль)', '3': 'весна(март)', '4': 'весна(апрель)', '5': 'весна(май)',
              '6': 'лето(июнь)', '7': 'лето(июль)', '8': 'лето(август)', '9': 'осень(сентябрь)', '10': 'осень(октябрь)',
              '11': 'осень(ноябрь)', '12': 'зима'
              }

if user_month >= 1 and user_month <= 12:
    print(month_dict.get(str(user_month)))
else:
    print('Введен не корретный номер месяца.Введите номер месяца от 1 до 12:')

month_list = ['зима(январь)', 'зима(февраль)','весна(март)','весна(апрель)','весна(май)','лето(июнь)','лето(июль)','лето(август)', 'осень(сентябрь)', 'осень(октябрь)',
              'осень(ноябрь)','зима']
print('*'*10, 'С помощью списка','*'*10 )
print(month_list[user_month-1])