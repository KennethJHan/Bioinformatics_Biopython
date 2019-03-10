#9.3.entrez.einfo_example.py

from Bio import Entrez

Entrez.email = "your@email.com"
handle = Entrez.einfo()
record = Entrez.read(handle)

print(record)

print(len(record["DbList"]))
