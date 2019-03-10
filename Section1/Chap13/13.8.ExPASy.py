#13.8.ExPASy.py
from Bio import ExPASy
from Bio import SwissProt

accession = "P04637"
handle = ExPASy.get_sprot_raw(accession)
record = SwissProt.read(handle)
print("gene_name:",record.gene_name)
print("organism:",record.organism)
print("sequence:",record.sequence)

