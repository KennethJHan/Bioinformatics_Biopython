#6.1.2.read_example_2.py

from Bio import SeqIO 

seq = SeqIO.read("sample_2.fasta", "fasta") 
print(type(seq)) 
print(seq) 

