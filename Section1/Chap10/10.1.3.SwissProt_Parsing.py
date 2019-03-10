#10.1.3.SwissProt_Parsing.py
from Bio import SwissProt

#https://www.uniprot.org/uniprot/P02649.txt
handle = open("P02649.txt")
record = SwissProt.read(handle)
print(type(record)) # <class 'Bio.SwissProt.Record'>
handle.close()

print(record.description)
print("gene_name:",record.gene_name)
print("organism:",record.organism)
print("sequence_length:",record.sequence_length)
print("sequence:",record.sequence)

