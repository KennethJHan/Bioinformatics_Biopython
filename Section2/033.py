#033.py

seq = "AGTTTATAG"
motif = "TT"
for i in range(len(seq)):
    if seq[i:i+len(motif)] == motif:
        print(i)
