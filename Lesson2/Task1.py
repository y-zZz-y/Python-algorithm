
while True:
    a = int(input('Введите число А: '))
    b = int(input('Введите число B: '))
    x = input('Введите операцию +, -, *, / или 0 для выхода: ')
    if x == '0':
        break
    elif x == '+':
        print(f'{a} + {b} = {a + b}')
    elif x == '-':
        print(f'{a} - {b} = {a - b}')
    elif x == '*':
        print(f'{a} * {b} = {a * b}')
    elif x == '/':
        if b == 0:
            print('На ноль делить нельзя!')
        else:
            print(f'{a} / {b} = {a / b}')