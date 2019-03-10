# 5.3.1.seqRecord_example.py 

from Bio.Seq import Seq 
from Bio.SeqRecord import SeqRecord 

seq = Seq("ACGT") 
seqRecord = SeqRecord(seq) 
print(seqRecord) 
print("----------") 

# SeqRecord 객체에 설명을 넣어준다. 
seqRecord.id = "NC_1111" 
seqRecord.name = "GeneA" 
seqRecord.description = "This is a description." 
seqRecord.annotations["Annotation_Key1"] = "Annotation_Value1" 
seqRecord.annotations["Annotation_Key2"] = "Annotation_Value2" 
print(seqRecord)

