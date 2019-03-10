#027-1.py

seq = "AGTTTATAG"
for s in seq[::3]:
#for s in seq[0:len(seq):3]: # seq[::3]과 같은 표현이다.
    print(s)
