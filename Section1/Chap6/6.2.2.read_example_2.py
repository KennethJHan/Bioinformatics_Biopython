#6.2.2.read_example2.py

import gzip 
from Bio import SeqIO 

with gzip.open("sample_1.fastq.gz","rt") as handle: 
    seq = SeqIO.parse(handle, "fastq") 
    for s in seq: 
        print(s.seq) 

