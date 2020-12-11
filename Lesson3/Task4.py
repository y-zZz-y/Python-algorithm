# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

cnt = {}
my_list = [randint(0,10) for el in range(30)]
print(my_list)

for el in my_list:
    if cnt.get(el):
        cnt.update({el:cnt[el]+1})
    else:
        cnt.update({el:1})
max = 0
for i in cnt:
    if cnt.get(max) < cnt.get(i):
        max = i

print(f'{max} встречается чаще всех')
