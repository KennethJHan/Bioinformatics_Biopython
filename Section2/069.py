#069.py

seq = "MLSSSMPPGGLACHADDDII"

d = {}

for s in seq:
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
        
print(d)
