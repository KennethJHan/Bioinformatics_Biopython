#9.4.entrez.esearch_example.py 

from Bio import Entrez 

Entrez.email = "your@email.com" 
handle = Entrez.esearch(db="pubmed", term="metagenome") 
record = Entrez.read(handle) 
print(record["Count"])  # 결과로 7020이 출력된다.

