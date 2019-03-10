#073.py

d = {'M': 2, 'L': 2, 'S': 3, 'P': 2, 'G': 2, 'A': 2, 'C': 1, 'H': 1, 'D': 3, 'I': 2}

d_sorted = sorted(d.items(), key=lambda v: v[1])

for k, v in d_sorted:
    print(k, v)
