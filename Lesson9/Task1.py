# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
#
# Примечания:
#
# * в сумму не включаем пустую строку и строку целиком;
#
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.

import hashlib
from itertools import combinations

def find_str(s: str, f_str: str) -> int: #поиск количества вхождений подстроки в строке
    assert len(s) > 0 and len(f_str) > 0, 'Строка не может быть пустой'
    assert len(s) > len(f_str), 'Строка не может быть меньше подстроки'

    f_str_len = len(f_str)
    f_str_hash = hashlib.sha1(f_str.encode('utf-8')).hexdigest()
    sss = 0
    for i in range(len(s)):
        if f_str_hash == hashlib.sha1(s[i:i+f_str_len].encode('utf-8')).hexdigest():
            sss += 1
    return sss

def find_index(s: str) -> int: #поиск различных комбинаций символов в строке
    assert len(s) > 0, 'Строка не может быть пустой'

    alph = [chr(el) for el in range(ord('a'), ord('z')+1)]
    alph_hash = [hashlib.sha1(chr(el).encode('utf-8')).hexdigest() for el in range(ord('a'), ord('z')+1)]
    sss = ''
    for j, el in enumerate(alph_hash):
        for i in range(len(s)):
            if el == hashlib.sha1(s[i:i + 1].encode('utf-8')).hexdigest():
                sss += alph[j]

    return len(set([''.join(l) for i in range(len(sss)) for l in combinations(sss, i + 1)]))-1, (len(sss)-2)*2

s = input('Введите строку: ')
f_str = input('Введите подстроку для поиска: ')

combi, mystr = find_index(s)

print(f'В строке {s} содержится {combi} различных комбинаций символов и {mystr} вариантов подстрок')
print(f'В строке {s} подстрока {f_str} содержится {find_str(s,f_str)} раз')