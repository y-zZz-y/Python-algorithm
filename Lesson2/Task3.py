# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

a = input('Введите число: ')
b = ''

for i in a:
    b = i + b

print(f'Обратный порядок: {b}')