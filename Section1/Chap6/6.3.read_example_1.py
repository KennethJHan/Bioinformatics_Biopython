#6.3.read_example_1.py 

from Bio import SeqIO 

gbk = SeqIO.read("KT225476.2.gbk","genbank") 
print(type(gbk)) 
print(gbk) 

