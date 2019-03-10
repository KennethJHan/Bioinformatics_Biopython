#8.3.1.blast_example_1.py 

from Bio.Blast import NCBIWWW 
from Bio import SeqIO 

record = SeqIO.read("buccal_swab.unmapped1.fasta", format="fasta") 
handle = NCBIWWW.qblast("blastn","nt",record.format("fasta")) 
result = handle.readlines() 
for s in result: 
    print(s) 

