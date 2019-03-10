#6.2.2.read_example_1.py
import gzip 
from Bio import SeqIO 
handle = gzip.open("sample_1.fastq.gz","rt") 
seq = SeqIO.parse(handle, "fastq") 
for s in seq: 
    print(s.seq) 

