#099.py

ts = 0 # A <-> G, C <-> T
tv = 0

with open("sample1.vcf","r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            l = line.split()
            ref = l[3]
            alt = l[4]
            if len(ref) == len(alt):
                if ref == "A":
                    if alt == "G":
                        ts += 1
                    else:
                        tv += 1
                elif ref == "C":
                    if alt == "T":
                        ts += 1
                    else:
                        tv += 1
                elif ref == "G":
                    if alt == "A":
                        ts += 1
                    else:
                        tv += 1
                elif ref == "T":
                    if alt == "C":
                        ts += 1
                    else:
                        tv += 1

print("transition:", ts)
print("transversion:", tv)
print("ts/tv:",ts/tv)
