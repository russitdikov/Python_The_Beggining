# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его
# же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()


def int_func_word(a):
    i = 0
    for letter in a:
        if ord(letter) < 97 or ord(letter) > 122:
            break
        else:
            i = 1
    if i == 1:
        return a.title()
    else:
        return 'Ошибка ввода. Слово должно состоять только из латинских маленьких букв.'


def init_function_str(a):
    word_str = a.split()
    word_str_cp = word_str.copy()
    for word in word_str:
        for letter in word:
            if ord(letter) < 97 or ord(letter) > 122:
                word_str_cp.remove(word)
                break
            else:
                continue
    final_list = ' '.join(word_str_cp)
    return final_list.title()


# print(int_func_word(input('Введите слово состоящее из латинских маленьких букв ')))
print(init_function_str(input('Введите слова состоящие из латинских маленьких букв, разделив их пробелом ')))
