#5.3.2.seqRecord_FASTA_example.py 

from Bio import SeqIO 

record = SeqIO.read("J01636.1.fasta","fasta") 
print(type(record)) 
print(record) 

