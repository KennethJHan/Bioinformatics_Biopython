# 4.4.2.gc_contents.py 
from Bio.Seq import Seq 

exon_seq = Seq("ATGCAGTAG") 
g_count = exon_seq.count("G") 
c_count = exon_seq.count("C") 
gc_contents = (g_count + c_count) / len(exon_seq) * 100 
print(gc_contents)  # 44.44 

