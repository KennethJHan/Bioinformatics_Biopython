#045.py

from random import randint

arr_lotto = []

for i in range(6):
    n = randint(1, 45)
    if n not in arr_lotto:
        arr_lotto.append(n)
        
for i in sorted(arr_lotto):
    print(i)
