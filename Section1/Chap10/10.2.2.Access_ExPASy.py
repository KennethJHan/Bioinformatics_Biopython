#10.2.2.Access_ExPASy.py
from Bio import ExPASy
from Bio import SwissProt

accession = "P02649"
handle = ExPASy.get_sprot_raw(accession)
record = SwissProt.read(handle)
print(record.gene_name)
print(record.organism)
print(record.sequence_length)
print(record.sequence)

