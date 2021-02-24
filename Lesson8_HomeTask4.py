# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5.Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на
# склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве
# единиц оргтехники, а также других данных, можно использовать любую подходящую
# структуру (например, словарь).
import os


class WrongAction(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:
    def __init__(self, wh_name, shielf_qnt, place_on_shielf_qnt):
        self.wh_name = wh_name
        self.shielf_max_qnt = 100
        self.shielf_qnt = shielf_qnt
        if int(self.shielf_qnt) > int(self.shielf_max_qnt):
            self.shielf_qnt = self.shielf_max_qnt
        self.place_on_shielf_qnt = place_on_shielf_qnt
        self.place = self.shielf_qnt * self.place_on_shielf_qnt
        with open(f'prt_in_{self.wh_name}.txt', 'w', encoding='utf-8') as wh_f:
            pass
        with open(f'scans_in_{self.wh_name}.txt', 'w', encoding='utf-8') as wh_f:
            pass
        with open(f'xerox_in_{self.wh_name}.txt', 'w', encoding='utf-8') as wh_f:
            pass
        with open(f'warhouse_{self.wh_name}.txt', 'w', encoding='utf-8') as wh_f:
            wh_f.writelines(f'WH_Name:{self.wh_name}\n')
            wh_f.writelines(f'shielf_qnt:{self.shielf_qnt}\n')
            wh_f.writelines(f'place_on_shielf_qnt:{self.place_on_shielf_qnt}\n')
            wh_f.writelines(f'idle_place:{self.place}\n')
            wh_f.writelines(f'prt_in_{self.wh_name}:prt_in_{self.wh_name}.txt\n')
            wh_f.writelines(f'scans_in_{self.wh_name}:scans_in_{self.wh_name}.txt\n')
            wh_f.writelines(f'xerox_in_{self.wh_name}:xerox_in_{self.wh_name}.txt\n')

    @classmethod
    def get_wh_exist(cls):
        cls.result = []
        cls.list = os.listdir(path='.')
        for i in cls.list:
            if i[:9] == 'warhouse_':
                cls.result.append(i[9:-4])
        return f'{cls.result}'

    @classmethod
    def get_wh_info(cls, name):
        cls.list = []
        cls.name = name
        with open(f'warhouse_{name}.txt', 'r', encoding='utf-8') as read_file:
            for i in read_file.readlines():
                cls.list.append(i.split(':')[1][:-1])
        cls.wh_dict = {'name': cls.list[0], 'shielf_qnt': cls.list[1], 'place_on_shielf_qnt': cls.list[2],
                       'idle_shielfs': cls.list[3]}
        print(cls.wh_dict)

    def wh_acceptance(self, equip_type):
        self.equip_type = equip_type


class Technics:
    def __init__(self, name, serial_number):
        self.name = name
        self.serial_number = serial_number
        self.status = 'purchased'
        self.wh_stored_name = 'na'
        self.shielf_stored_number = 'na'
        self.depat_transf = 'na'

    @classmethod
    def printer_qnt(cls):
        cls.list = []
        cls.purchased_count = 0
        cls.in_the_wh_count = 0
        cls.in_dept = 0
        with open(f'printers.txt', 'r', encoding='utf-8') as read_f:
            for i in read_f.readlines():
                cls.list.append(i.split(' '))
                if i.find('purchased') != -1:
                    cls.purchased_count += 1
                elif i.find('in_the_wh') != -1:
                    cls.in_the_wh_count += 1
                elif i.find('in_dept') != -1:
                    cls.in_dept += 1
            print(f'В настоящий момент в базе {len(cls.list)} объекта. \n '
                  f'Из них на не оприходованно - {cls.purchased_count} шт.,\n '
                  f'на складе - {cls.in_the_wh_count} шт.,\n '
                  f'в пользовании в подразделениях - {cls.in_dept} шт. ')


class Printer(Technics):
    def __init__(self, name, serial_number):
        super().__init__(name, serial_number)
        self.checkval = 0
        with open(f'printers.txt', 'r') as read_f:
            for i in read_f.readlines():
                if i.find(name) != -1:
                    print('Объект с таким именем уже имеется в БД. Запись в БД не может создан повторно')
                    self.checkval = 1
        if self.checkval == 0:
            with open(f'printers.txt', 'a', encoding='utf-8') as prt_f:
                prt_f.writelines(f'Printer_name:{self.name} ')
                prt_f.writelines(f'serial_number:{self.serial_number} ')
                prt_f.writelines(f'status:{self.status} ')
                prt_f.writelines(f'WH_stored_name:{self.wh_stored_name}\n')
            print('Объект успесшно добавлен в БД')

    @classmethod
    def get_oblect_name(cls):
        objects_name = []
        with open('printers.txt', 'r', encoding='utf-8') as read_file:
            for i in read_file.readlines():
                objects_name.append(i.split(' ')[0].split(':')[1])
        return f'{objects_name} '

    @classmethod
    def to_wh_tranfer(cls, name):
        cls.name = name
        cls.list = []
        """передача принтера со склада на склад.открываем список имеющихся принтеров"""
        with open(f'printers.txt', 'r', encoding='utf-8') as read_f:
            lines = read_f.readlines()
            words = []
            for i in lines:
                if not i.isspace():
                    words.append(i.split(' '))
            for word in words:
                """если имя принтера есть в перечне принтеров запрашиваем имя склада на который необходимо принтер добавить"""
                if word[0][13:] == name:
                    wh_for_storage = input(
                        f'Для передачи объекта {cls.name} выберите один из доступных складов :{Warehouse.get_wh_exist()}. Введите его имя:')
                    check_val = 0
                    """Проверяем соответствует ли введенное пользователем значение какому либо из существующих складов"""
                    while check_val == 0:
                        if len(wh_for_storage) < 3:
                            wh_for_storage = input(
                                f'Имя введено не корректно. Выберите один из доступных складов :{Warehouse.get_wh_exist()}. Введите его имя:')
                        else:
                            try:
                                if Warehouse.get_wh_exist().count(wh_for_storage) == 1:
                                    check_val = 1
                                else:
                                    wh_for_storage = input(
                                        f'Имя введено не корректно. Выберите один из доступных складов :{Warehouse.get_wh_exist()}. Введите его имя:')
                            except ValueError:
                                wh_for_storage = input(
                                    f'Имя введено не корректно. Выберите один из доступных складов :{Warehouse.get_wh_exist()}. Введите его имя:')
                    """проверяем, не хранится ли уже указанный принтер на указанном складе"""
                    if word[3][15:-1] != wh_for_storage:
                        if word[3][15:-1] != 'na':
                            """открываем файл принтеров на старом складе и сохраняем в списке все принтеры, кроме передаваемого"""
                            with open(f'prt_in_{word[3][15:-1]}.txt', 'r', encoding='utf-8') as old_wh_f:
                                old_wh = old_wh_f.readlines()
                                obj_info = [prt.split() for prt in old_wh if
                                            not prt.isspace() and prt.split()[0][13:] != cls.name]
                            with open(f'prt_in_{word[3][15:-1]}.txt', 'w', encoding='utf-8') as old_wh_f:
                                for i in obj_info:
                                    old_wh_f.writelines(' '.join(i) + '\n')
                            """уменьшаем количество свободных ячеек на складе, где лежал принтер"""
                            with open(f'warhouse_{word[3][15:-1]}.txt', 'r+', encoding='utf-8') as exist_wh_f:
                                exist_wh_descr = exist_wh_f.readlines()
                                if int(exist_wh_descr[3][11:-1]) < 10000:
                                    print(exist_wh_descr, exist_wh_descr[3][11:-1])
                                    exist_wh_descr[3] = f'idle_place:{int(exist_wh_descr[3][11:-1]) + 1}\n'
                                    exist_wh_f.seek(0, 0)
                                    exist_wh_f.writelines(exist_wh_descr, )
                        """в файле со списком принтеров меняем статус и перезаписываем файл в котором принтер имеет уже обновленный статус"""
                        word[3] = word[3].replace(word[3], f'WH_stored_name:{wh_for_storage}\n')
                        word[2] = word[2].replace('purchased', 'in_the_wh')
                        with open(f'prt_in_{wh_for_storage}.txt', 'a', encoding='utf-8') as prt_f_wh:
                            prt_f_wh.writelines(' '.join(word))
                        with open(f'warhouse_{wh_for_storage}.txt', 'r+', encoding='utf-8') as new_wh_f:
                            wh_descr = new_wh_f.readlines()
                            if int(wh_descr[3][11:-1]) > 0:
                                wh_descr[3] = f'idle_place:{int(wh_descr[3][11:-1]) - 1}\n'
                                new_wh_f.seek(0, 0)
                                new_wh_f.writelines(wh_descr)
                            else:
                                print('Склад заполнен. Выберите другой склад')
                        with open(f'printers.txt', 'w') as prt_f:
                            for word in words:
                                prt_f.writelines(' '.join(word))
                        print(f'Объект {cls.name} успешно передан на склад {wh_for_storage}')
                        return ''
                    else:
                        print(f'Данный уже на складе {wh_for_storage}')
                        return ''
            print(f'Данного объекта нет в списке. Полный список имющихся объектов:{Printer.get_oblect_name()}')
            return ''


class Scanner(Technics):
    def __init__(self, name, serial_number):
        super().__init__(name, serial_number)
        self.checkval = 0
        with open(f'scanners.txt', 'r') as read_f:
            for i in read_f.readlines():
                if i.find(name) != -1:
                    print('Объект с таким именем уже имеется в БД. Запись в БД не может создан повторно')
                    self.checkval = 1
        if self.checkval == 0:
            with open(f'scanners.txt', 'a', encoding='utf-8') as prt_f:
                prt_f.writelines(f'scanner_name:{self.name} ')
                prt_f.writelines(f'serial_number:{self.serial_number} ')
                prt_f.writelines(f'status:{self.status} ')
                prt_f.writelines(f'WH_stored_name:{self.wh_stored_name}\n')
            print('Объект успесшно добавлен в БД')

    @classmethod
    def get_oblect_name(cls):
        objects_name = []
        with open('scanners.txt', 'r', encoding='utf-8') as read_file:
            for i in read_file.readlines():
                objects_name.append(i.split(' ')[0].split(':')[1])
        return f'{objects_name} '

    @classmethod
    def to_wh_tranfer(cls, name):
        cls.name = name
        cls.list = []
        """передача принтера со склада на склад.открываем список имеющихся принтеров"""
        with open(f'scanners.txt', 'r', encoding='utf-8') as read_f:
            lines = read_f.readlines()
            words = []
            for i in lines:
                if not i.isspace():
                    words.append(i.split(' '))
            for word in words:
                """если имя принтера есть в перечне принтеров запрашиваем имя склада на который необходимо принтер добавить"""
                if word[0][13:] == name:
                    wh_for_storage = input(
                        f'Для передачи объекта {cls.name} выберите один из доступных складов :{Warehouse.get_wh_exist()}. Введите его имя:')
                    check_val = 0
                    """Проверяем соответствует ли введенное пользователем значение какому либо из существующих складов"""
                    while check_val == 0:
                        if len(wh_for_storage) < 3:
                            wh_for_storage = input(
                                f'Имя введено не корректно. Выберите один из доступных складов :{Warehouse.get_wh_exist()}. Введите его имя:')
                        else:
                            try:
                                if Warehouse.get_wh_exist().count(wh_for_storage) == 1:
                                    check_val = 1
                                else:
                                    wh_for_storage = input(
                                        f'Имя введено не корректно. Выберите один из доступных складов :{Warehouse.get_wh_exist()}. Введите его имя:')
                            except ValueError:
                                wh_for_storage = input(
                                    f'Имя введено не корректно. Выберите один из доступных складов :{Warehouse.get_wh_exist()}. Введите его имя:')
                    """проверяем, не хранится ли уже указанный принтер на указанном складе"""
                    if word[3][15:-1] != wh_for_storage:
                        if word[3][15:-1] != 'na':
                            """открываем файл принтеров на старом складе и сохраняем в списке все принтеры, кроме передаваемого"""
                            with open(f'scans_in_{word[3][15:-1]}.txt', 'r', encoding='utf-8') as old_wh_f:
                                old_wh = old_wh_f.readlines()
                                obj_info = [scans.split() for scans in old_wh if
                                            not scans.isspace() and scans.split()[0][13:] != cls.name]
                            with open(f'scans_in_{word[3][15:-1]}.txt', 'w', encoding='utf-8') as old_wh_f:
                                for i in obj_info:
                                    old_wh_f.writelines(' '.join(i) + '\n')
                            """уменьшаем количество свободных ячеек на складе, где лежал принтер"""
                            with open(f'warhouse_{word[3][15:-1]}.txt', 'r+', encoding='utf-8') as exist_wh_f:
                                exist_wh_descr = exist_wh_f.readlines()
                                if int(exist_wh_descr[3][11:-1]) < 10000:
                                    print(exist_wh_descr, exist_wh_descr[3][11:-1])
                                    exist_wh_descr[3] = f'idle_place:{int(exist_wh_descr[3][11:-1]) + 1}\n'
                                    exist_wh_f.seek(0, 0)
                                    exist_wh_f.writelines(exist_wh_descr)
                        """в файле со списком принтеров меняем статус и перезаписываем файл в котором принтер имеет уже обновленный статус"""
                        word[3] = word[3].replace(word[3], f'WH_stored_name:{wh_for_storage}\n')
                        word[2] = word[2].replace('purchased', 'in_the_wh')
                        with open(f'scans_in_{wh_for_storage}.txt', 'a', encoding='utf-8') as prt_f_wh:
                            prt_f_wh.writelines(' '.join(word))
                        with open(f'warhouse_{wh_for_storage}.txt', 'r+', encoding='utf-8') as new_wh_f:
                            wh_descr = new_wh_f.readlines()
                            if int(wh_descr[3][11:-1]) > 0:
                                wh_descr[3] = f'idle_place:{int(wh_descr[3][11:-1]) - 1}\n'
                                new_wh_f.seek(0, 0)
                                new_wh_f.writelines(wh_descr)
                            else:
                                print('Склад заполнен. Выберите другой склад')
                        with open(f'scanners.txt', 'w') as scs_f:
                            for word in words:
                                scs_f.writelines(' '.join(word))
                        print(f'Объект {cls.name} успешно передан на склад {wh_for_storage}')
                        return ''
                    else:
                        print(f'Данный уже на складе {wh_for_storage}')
                        return ''
            print(f'Данного объекта нет в списке. Полный список имющихся объектов:{Scanner.get_oblect_name()}')
            return ''


class Xerox(Technics):
    def __init__(self, name, serial_number):
        super().__init__(name, serial_number)
        self.checkval = 0
        with open(f'xerox.txt', 'r') as read_f:
            for i in read_f.readlines():
                if i.find(name) != -1:
                    print('Объект с таким именем уже имеется в БД. Запись в БД не может создан повторно')
                    self.checkval = 1
        if self.checkval == 0:
            with open(f'xerox.txt', 'a', encoding='utf-8') as prt_f:
                prt_f.writelines(f'xerox_name:{self.name} ')
                prt_f.writelines(f'serial_number:{self.serial_number} ')
                prt_f.writelines(f'status:{self.status} ')
                prt_f.writelines(f'WH_stored_name:{self.wh_stored_name}\n')
            print('Объект успесшно добавлен в БД')

    @classmethod
    def get_oblect_name(cls):
        objects_name = []
        with open('xerox.txt', 'r', encoding='utf-8') as read_file:
            for i in read_file.readlines():
                objects_name.append(i.split(' ')[0].split(':')[1])
        return f'{objects_name} '

    @classmethod
    def to_wh_tranfer(cls, name):
        cls.name = name
        cls.list = []
        """передача принтера со склада на склад.открываем список имеющихся принтеров"""
        with open(f'xerox.txt', 'r', encoding='utf-8') as read_f:
            lines = read_f.readlines()
            words = []
            for i in lines:
                if not i.isspace():
                    words.append(i.split(' '))
            for word in words:
                """если имя принтера есть в перечне принтеров запрашиваем имя склада на который необходимо принтер добавить"""
                if word[0][11:] == name:
                    wh_for_storage = input(
                        f'Для передачи объекта {cls.name} выберите один из доступных складов :{Warehouse.get_wh_exist()}. Введите его имя:')
                    check_val = 0
                    """Проверяем соответствует ли введенное пользователем значение какому либо из существующих складов"""
                    while check_val == 0:
                        if len(wh_for_storage) < 3:
                            wh_for_storage = input(
                                f'Имя введено не корректно. Выберите один из доступных складов :{Warehouse.get_wh_exist()}. Введите его имя:')
                        else:
                            try:
                                if Warehouse.get_wh_exist().count(wh_for_storage) == 1:
                                    check_val = 1
                                else:
                                    wh_for_storage = input(
                                        f'Имя введено не корректно. Выберите один из доступных складов :{Warehouse.get_wh_exist()}. Введите его имя:')
                            except ValueError:
                                wh_for_storage = input(
                                    f'Имя введено не корректно. Выберите один из доступных складов :{Warehouse.get_wh_exist()}. Введите его имя:')
                    """проверяем, не хранится ли уже указанный принтер на указанном складе"""
                    if word[3][15:-1] != wh_for_storage:
                        if word[3][15:-1] != 'na':
                            """открываем файл принтеров на старом складе и сохраняем в списке все принтеры, кроме передаваемого"""
                            with open(f'xerox_in_{word[3][15:-1]}.txt', 'r', encoding='utf-8') as old_wh_f:
                                old_wh = old_wh_f.readlines()
                                obj_info = [scans.split() for scans in old_wh if
                                            not scans.isspace() and scans.split()[0][13:] != cls.name]
                            with open(f'xerox_in_{word[3][15:-1]}.txt', 'w', encoding='utf-8') as old_wh_f:
                                for i in obj_info:
                                    old_wh_f.writelines(' '.join(i) + '\n')
                            """уменьшаем количество свободных ячеек на складе, где лежал принтер"""
                            with open(f'warhouse_{word[3][15:-1]}.txt', 'r+', encoding='utf-8') as exist_wh_f:
                                exist_wh_descr = exist_wh_f.readlines()
                                if int(exist_wh_descr[3][11:-1]) < 10000:
                                    print(exist_wh_descr, exist_wh_descr[3][11:-1])
                                    exist_wh_descr[3] = f'idle_place:{int(exist_wh_descr[3][11:-1]) + 1}\n'
                                    exist_wh_f.seek(0, 0)
                                    exist_wh_f.writelines(exist_wh_descr)
                        """в файле со списком принтеров меняем статус и перезаписываем файл в котором принтер имеет уже обновленный статус"""
                        word[3] = word[3].replace(word[3], f'WH_stored_name:{wh_for_storage}\n')
                        word[2] = word[2].replace('purchased', 'in_the_wh')
                        with open(f'xerox_in_{wh_for_storage}.txt', 'a', encoding='utf-8') as prt_f_wh:
                            prt_f_wh.writelines(' '.join(word))
                        with open(f'warhouse_{wh_for_storage}.txt', 'r+', encoding='utf-8') as new_wh_f:
                            wh_descr = new_wh_f.readlines()
                            if int(wh_descr[3][11:-1]) > 0:
                                wh_descr[3] = f'idle_place:{int(wh_descr[3][11:-1]) - 1}\n'
                                new_wh_f.seek(0, 0)
                                new_wh_f.writelines(wh_descr)
                            else:
                                print('Склад заполнен. Выберите другой склад')
                        with open(f'xerox.txt', 'w') as scs_f:
                            for word in words:
                                scs_f.writelines(' '.join(word))
                        print(f'Объект {cls.name} успешно передан на склад {wh_for_storage}')
                        return ''
                    else:
                        print(f'Данный уже на складе {wh_for_storage}')
                        return ''
            print(f'Данного объекта нет в списке. Полный список имющихся объектов:{Xerox.get_oblect_name()}')
            return ''


# wh1 = Warehouse('WH1',101,100)
# wh2 = Warehouse('WH2',101,100)
# wh3 = Warehouse('WH3',100,100)

# print(Warehouse.get_wh_exist())
# wh1.get_wh_info('WH1')
# printer1 = Printer('printer_1', '001')
# printer2 = Printer('printer_2', '002')
# printer3 = Printer('printer_3', '003')

# print(Warehouse.get_wh_exist())
# Printer.printer_qnt()
# wh1.get_wh_info('WH1')

# Printer.to_wh_tranfer('printer_1')
# Printer.to_wh_tranfer('printer_2')#в файле prt_in_WH2 сначала появляется пустая строка
# Printer.to_wh_tranfer('printer_3')
# Printer.printer_qnt()

# scanner1=Scanner('scanner_1','001')
# Scanner.to_wh_tranfer('scanner_1')

# xerox1 = Xerox('xerox_1','001')
# xerox2 = Xerox('xerox_2','002')
Xerox.to_wh_tranfer('xerox_2')
