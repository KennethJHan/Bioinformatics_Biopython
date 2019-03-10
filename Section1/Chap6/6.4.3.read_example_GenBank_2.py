#6.4.3.read_example_GenBank_2.py 

from Bio import Entrez 
from Bio import SeqIO 

Entrez.email = "your@email.com"

with Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id="1575550") as handle: 
    seq = SeqIO.read(handle, "fasta") 
     
print(seq) 
print(len(seq)) 

