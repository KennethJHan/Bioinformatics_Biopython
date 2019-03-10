#100.py

length = 0

with open("sample1.bed","r") as fr:
    for line in fr:
        l = line.strip().split()
        start = int(l[1])
        end = int(l[2])
        length += end - start
        
print(length)
