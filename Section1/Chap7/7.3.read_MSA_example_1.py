#7.3.read_MSA_example_1.py
from Bio import AlignIO 

alignment = AlignIO.read("example.aln","clustal") 
for record in alignment: 
    print("%s - %s" % (record.seq, record.id))
