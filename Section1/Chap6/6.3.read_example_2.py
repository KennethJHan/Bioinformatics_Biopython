#6.3.read_example_2.py 

from Bio import SeqIO 

gbk = SeqIO.read("KT225476.2.gbk","genbank") 
print(gbk.id) 
print(gbk.description) 
print(gbk.annotations['molecule_type']) 
print(gbk.annotations['organism']) 

