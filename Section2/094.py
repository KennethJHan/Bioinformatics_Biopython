#094.py

with open("sample1.vcf","r") as fr:
    for line in fr:
        if line.startswith("#CHROM"):
            print(len(line.split()) - 9)

