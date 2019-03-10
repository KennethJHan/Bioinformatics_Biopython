# 4.4.7.complement.bio.py 
from Bio.Seq import Seq 

seq = Seq("TATAAAGGCAATATGCAGTAG") 
comp_seq = seq.complement() 
rev_comp_seq = seq.reverse_complement() 
print(comp_seq)  # ATATTTCCGTTATACGTCATC 
print(rev_comp_seq)  # CTACTGCATATTGCCTTTATA 

