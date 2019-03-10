#5.4.compare_example_4.py

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

seq1 = Seq("ACGT")
record1 = SeqRecord(seq1)

seq2 = Seq("ACGT")
record2 = SeqRecord(seq2)

print(record1.seq == record2.seq)  # True가 출력된다.

