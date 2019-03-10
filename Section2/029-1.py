#029-1.py
seq = "AGTTTATAG"
rev_seq = ""
for i in range(len(seq)-1,-1,-1):
    rev_seq += seq[i]
print(rev_seq)
