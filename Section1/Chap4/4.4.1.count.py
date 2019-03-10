# 4.4.1.count.py 
from Bio.Seq import Seq 

exon_seq = Seq("ATGCAGTAG") 
count_a = exon_seq.count("A") 
print(count_a) # 3 이 출력된다. 
