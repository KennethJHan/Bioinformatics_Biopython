#030.py
seq = "AGTTTATAG"
new_seq = ""
for s in seq:
    if s == "A":
        new_seq += "T"
    elif s == "C":
        new_seq += "G"
    elif s == "G":
        new_seq += "C"
    elif s == "T":
        new_seq += "A"
print(new_seq)
