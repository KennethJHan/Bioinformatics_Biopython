#098.py

rs = 0

with open("sample1.vcf","r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            l = line.split()
            rsID = l[2]
            if rsID != ".":
                rs += 1

print(rs)
