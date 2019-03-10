#6.4.3.read_example_GenBank_1.py 

from Bio import Entrez 
from Bio import SeqIO 

Entrez.email = "kenneth.jh.han@gmail.com" 

with Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id="42540826") as handle: 
    seq = SeqIO.read(handle, "fasta") 
     
print(seq) 
print(len(seq)) 

