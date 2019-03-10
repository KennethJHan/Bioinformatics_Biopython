#5.3.3.seqRecord_GenBank_example.py 

from Bio import SeqIO 

record = SeqIO.read("J01636.1.gbk","genbank") 
print(type(record)) 
print(record) 

