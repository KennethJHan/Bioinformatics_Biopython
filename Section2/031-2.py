#031-2.py
from Bio.Seq import Seq

seq = Seq("AGTTTATAG")
print(seq)
print(seq.reverse_complement())
