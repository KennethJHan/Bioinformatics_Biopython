#9.2.1.efetch_example.py 

from Bio import Entrez 

Entrez.email = "your@email.com" # 자신의 이메일을 사용해야 한다. 
handle = Entrez.efetch(db="nucleotide", id="NC_002058.3", rettype="gb", retmode="text") 
print(handle.read())
