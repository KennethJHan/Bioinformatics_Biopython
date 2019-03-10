#7.3.read_MSA_example_2.py

from Bio import AlignIO 

alignment = AlignIO.read("example.aln","clustal") 
for record in alignment: 
    print("%s - %s" % (record.seq[:10], record.id)) 
