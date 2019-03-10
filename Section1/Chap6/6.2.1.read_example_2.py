#6.2.1.read_example_2.py 

from Bio import SeqIO 

seq = SeqIO.parse("sample_1.fastq", "fastq") 
for s in seq: 
    print(s.seq) 

