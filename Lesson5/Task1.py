# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.

# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

firms = []
new_firm = namedtuple('new_firm', 'name, profit1, profit2, profit3, profit4, avg, profit_sum', defaults=[0,0,0,0,0])
profit_sum = 0

while True:
    prop = input('Введите наименование предприятия и прибыль за 4 квартала через пробел, для завершения введите 0: ').split()
    if prop[0] == '0':
        break
    for i, el in enumerate(prop):
        if i:
            prop[i] = int(el)
    try:
        firms.append(new_firm(*prop,sum(prop[1:])/12,sum(prop[1:])))
    except:
        print('Ошибка ввода данных')

    profit_sum += sum(prop[1:])

profit_avg = profit_sum/len(firms)

max_profit = []
min_profit = []

for i in firms:
    if i.profit_sum > profit_avg:
        max_profit.append(i.name)
    else:
        min_profit.append(i.name)

print(f'Предприятия с прибылью выше среднего: {max_profit}')
print(f'Предприятия с прибылью ниже среднего: {min_profit}')

