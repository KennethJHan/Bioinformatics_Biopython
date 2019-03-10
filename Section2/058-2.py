#058-2.py

a = [3, 5, 2, 1, 4]

max_val = a[0]

for i in range(1,len(a)):
    if max_val < a[i]:
        max_val = a[i]

print(max_val)
