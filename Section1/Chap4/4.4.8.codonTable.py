# 4.4.8.codonTable.py 
from Bio.Data import CodonTable 

codon_table = CodonTable.unambiguous_dna_by_name["Standard"] 
print(codon_table) 

