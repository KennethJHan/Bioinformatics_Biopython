#6.1.1.parse_example_1.py 

from Bio import SeqIO 

seq = SeqIO.parse("sample_2.fasta", "fasta") 
print(type(seq)) 
for s in seq:
    print(type(s))
    print(s)
    print("") # 줄 구분을 위해 넣었다. 

