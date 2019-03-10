#9.2.2.entrez_parse_example.py 

from Bio import Entrez 

Entrez.email = "your@email.com"
handle = Entrez.efetch(db="nucleotide", id="NC_002058.3", rettype="gb", retmode="xml") 
records = Entrez.parse(handle) 
for record in records: 
    for journal in record["GBSeq_references"]: 
        print(journal["GBReference_title"]) 

