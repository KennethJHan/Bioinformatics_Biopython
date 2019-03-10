#9.2.2.entrez_read_example.py 

from Bio import Entrez 

Entrez.email = "your@email.com"
handle = Entrez.efetch(db="nucleotide", id="NC_002058.3", rettype="gb", retmode="xml") 
records = Entrez.read(handle) 
for record in records: 
    print(record["GBSeq_locus"]) 
    print(record["GBSeq_definition"]) 
    print(record["GBSeq_strandedness"], record["GBSeq_moltype"])
    print(record["GBSeq_length"], "bp") 
    print(len(record["GBSeq_references"]), "journals") 

