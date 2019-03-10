#13.7.efetch.py 

from Bio import Entrez 

Entrez.email = "your@email.com"
handle = Entrez.efetch(db="nucleotide", id="NC_001498.1", rettype="gb", retmode="xml") 
records = Entrez.read(handle) 
for record in records: 
    print("Locus:",record["GBSeq_locus"]) 
    print("Definition:",record["GBSeq_definition"]) 
    print("Strand, Molecular type:",record["GBSeq_strandedness"], record["GBSeq_moltype"])
    print("Length:",record["GBSeq_length"], "bp") 
    print("Journal:",len(record["GBSeq_references"]), "journals") 

