#031-1.py

seq = "AGTTTATAG"
rev_seq = seq[::-1]
revcomp_seq = ""
for s in rev_seq:
    if s == "A":
        revcomp_seq += "T"
    elif s == "C":
        revcomp_seq += "G"
    elif s == "G":
        revcomp_seq += "C"
    elif s == "T":
        revcomp_seq += "A"
print(seq)
print(revcomp_seq)
