# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

class Date:
    def __init__(self, date, mounth, year):
        self.date = date
        self.mounth = mounth
        self.year = year

    @classmethod
    def decomposite(cls, us_date):
        ud = us_date
        date_decomp = ud.split('-')
        if len(date_decomp) == 3:
            try:
                for i in date_decomp:
                    int(i)
                print(f'date_decomposit_result:{int(date_decomp[0])}')
                date, mounth, year = date_decomp
                return cls(date, mounth, year)
            except:
                print('date_decomposit_result:дата введена не корректно. используйте арабские цифры для ввода')
        else:
            print('date_decomposit_result:дата введена не корректно. необходимо ввести в формате дд-мм-гггг')

    @staticmethod
    def date_validation(obj):
        try:
            if 0 < int(obj.date) < 32:
                print('date_validation_result:Число валидно')
            else:
                print('date_validation_result:Число не валидно')

            if 0 < int(obj.mounth) < 13:
                return 'date_validation_result:Месяц валиден'
            else:
                return 'date_validation_result:Месяц не валиден'
        except:
            return 'date_validation_result:дата введена не корректно'


user_date = input('введите число в формате дд-мм-гггг: ')

date1 = Date.decomposite(user_date)

print(Date.date_validation(date1))
