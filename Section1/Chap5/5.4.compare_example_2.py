#5.4.compare_example_2.py

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

seq1 = Seq("ACGT")
record1 = SeqRecord(seq1)
print(record1)

print("----------")

seq2 = Seq("ACGT")
record2 = SeqRecord(seq2)
print(record2)

