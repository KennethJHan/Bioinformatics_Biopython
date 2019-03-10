# 5.1.simple_seqrecord_object_example_3.py 

from Bio.Seq import Seq 
from Bio.SeqRecord import SeqRecord 

simple_seq = Seq("ACGT") 
simple_seqRecord = SeqRecord(simple_seq, id="NC_1111", name="Test") 
simple_seqRecord.name = "Another name" 

print(simple_seqRecord) 

