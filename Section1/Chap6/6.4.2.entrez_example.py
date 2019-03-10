#6.4.2.entrez_example.py 

from Bio import Entrez 

Entrez.email = "kenneth.jh.han@gmail.com" 
handle = Entrez.efetch(db="nucleotide", rettype="gb", id="AY463215", retmode="text") 

for s in handle: 
    print(s.strip())
