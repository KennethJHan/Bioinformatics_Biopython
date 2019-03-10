#095.py

cnt = 0

with open("sample1.vcf","r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            l = line.split()
            if l[6] == "PASS":
                cnt += 1

print(cnt)
