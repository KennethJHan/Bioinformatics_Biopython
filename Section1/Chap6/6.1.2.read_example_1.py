#6.1.2.read_example_1.py

from Bio import SeqIO 

seq = SeqIO.read("sample_1.fasta", "fasta") 
print(type(seq)) 
print(seq)
