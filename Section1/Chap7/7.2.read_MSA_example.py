#7.2.read_MSA_example.py 

from Bio import AlignIO 

alignment = AlignIO.read("example.aln","clustal") 
print(alignment) 
