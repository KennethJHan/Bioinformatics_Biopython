#096.py

variants = 0

with open("sample1.vcf","r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            variants += 1

print(variants)
