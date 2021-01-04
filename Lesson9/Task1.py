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

def find_index(s: str) -> int:
    assert len(s) > 0, 'Строка не может быть пустой'

    alph = [chr(el) for el in range(ord('a'), ord('z')+1)]
    alph_hash = [hashlib.sha1(chr(el).encode('utf-8')).hexdigest() for el in range(ord('a'), ord('z')+1)]
    sss = ''
    for j, el in enumerate(alph_hash):
        for i in range(len(s)):
            if el == hashlib.sha1(s[i:i + 1].encode('utf-8')).hexdigest():
                sss += alph[j]

    return len(set([''.join(l) for i in range(len(sss)) for l in combinations(sss, i + 1)]))-1

s = input('Введите строку: ')

print(f'В строке {s} содержится {find_index(s)} различных подсрок')