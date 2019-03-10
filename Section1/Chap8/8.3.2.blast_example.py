#8.3.2.blast_example.py

from Bio.Blast import NCBIWWW 
from Bio.Blast import NCBIXML 
from Bio import SeqIO 

record = SeqIO.read("buccal_swab.unmapped1.fasta", format="fasta") 
handle = NCBIWWW.qblast("blastn","nt",record.format("fasta")) 

blast_records = NCBIXML.parse(handle) 
E_VALUE_THRESHOLD = 0.05 
for blast_record in blast_records: 
    for alignment in blast_record.alignments: 
        for hsp in alignment.hsps: 
            if hsp.expect < E_VALUE_THRESHOLD: 
                print(alignment.title) 
                print(alignment.length) 
                print(hsp.expect) 
                print(hsp.query[0:75]) 
                print(hsp.match[0:75]) 
                print(hsp.sbjct[0:75]) 

