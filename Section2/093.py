#093.py

header = ""
data = ""

with open("sample1.vcf","r") as fr:
    for line in fr:
        if line.startswith("#"):
            header += line
        else:
            data += line
print(header)
print("")
print(data)
