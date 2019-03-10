# 4.3.1.make_sequence.py 
from Bio.Seq import Seq 

tatabox_seq = Seq("tataaaggcAATATGCAGTAG") 
print(tatabox_seq) # tataaaggcAATATGCAGTAG 가 출력된다. 
print(type(tatabox_seq)) # <class 'Bio.Seq.Seq'> 
