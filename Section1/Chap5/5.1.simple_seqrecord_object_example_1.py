# 5.1.simple_seqrecord_object_example_1.py 

from Bio.Seq import Seq 
from Bio.SeqRecord import SeqRecord # Bio.SeqRecord에서 SeqRecord를 import 하였다. 

seq = Seq("ACGT") # 먼저 Sequence 객체를 만든다. 
seqRecord = SeqRecord(seq) # SeqRecord 객체를 만든다. 

print(seqRecord) 

