#9.3.entrez_example_1.py 

from Bio import Entrez 

Entrez.email = "your@email.com" 
handle = Entrez.einfo() 
result = handle.read() 
print(result) 

