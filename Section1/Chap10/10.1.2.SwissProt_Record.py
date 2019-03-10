#10.1.2.SwissProt_Record.py
from Bio import SwissProt
#https://www.uniprot.org/uniprot/P02649.txt
handle = open("P02649.txt")
record = SwissProt.read(handle)
print(type(record)) # <class 'Bio.SwissProt.Record'>
handle.close()

