#059-2.py

a = [3, 5, 2, 1, 4]

min_val = a[0]

for i in range(1,len(a)):
    if min_val > a[i]:
        min_val = a[i]

print(min_val)
