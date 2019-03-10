#6.2.1.read_example_1.py 

from Bio import SeqIO 

seq = SeqIO.parse("sample_1.fastq", "fastq") 
print(type(seq)) 
for s in seq: 
    print(type(s)) 
    print(s) 
    print("") # 줄 구분을 위해 넣었다. 

