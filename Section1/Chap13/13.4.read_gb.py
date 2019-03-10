#13.4.read_gb.py 

from Bio import SeqIO 

gbk = SeqIO.read("NM_000384.2.gb","genbank") 
print("id:",gbk.id)
print("description:",gbk.description)
print("molecule_type:",gbk.annotations['molecule_type'])
print("organism:",gbk.annotations['organism'])
