# 13.3.rev_comp.py 
from Bio.Seq import Seq 

seq = Seq("ACATTA") 
comp_seq = seq.complement() 
rev_comp_seq = seq.reverse_complement() 
print("comp_seq:",comp_seq)  # TGTAAT
print("rev_comp_seq:",rev_comp_seq)  # TAATGT 

