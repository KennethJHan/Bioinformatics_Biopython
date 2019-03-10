# 5.1.simple_seqrecord_object_example_2.py 

from Bio.Seq import Seq 
from Bio.SeqRecord import SeqRecord 

simple_seq = Seq("ACGT") 
simple_seqRecord = SeqRecord(simple_seq, id="NC_1111", name="Test") 
# SeqRecord 객체를 만들 때, id와 name에 각각 값을 집어넣었다. 

print(simple_seqRecord) 

