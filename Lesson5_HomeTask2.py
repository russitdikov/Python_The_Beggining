# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
# строк, количества слов в каждой строке.
line_count = 0
with open('text_l5_ht1.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        line_count += 1
        word_count = 0
        f_line = line.split()
        for word in f_line:
            word_count += 1
        print(f'количество слов в строке {line_count}: {word_count}')
print(f'количество строк: {line_count}')
