#092.py

count = 0

with open("sample1.fasta","r") as fr:
    for line in fr:
        if line.startswith(">"):
            count += 1
            
print(count)
