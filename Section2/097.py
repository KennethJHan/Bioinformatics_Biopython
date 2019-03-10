#097.py

SNP = 0
Insertion = 0
Deletion = 0

with open("sample1.vcf","r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            l = line.split()
            ref = l[3]
            alt = l[4]
            
            if len(ref) == len(alt):
                SNP += 1
            elif len(ref) > len(alt):
                Deletion += 1
            elif len(ref) < len(alt):
                Insertion += 1

print("SNP:", SNP)
print("Insertion:", Insertion)
print("Deletion:", Deletion)
