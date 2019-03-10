# 4.4.3.case.py 
from Bio.Seq import Seq 

tatabox_seq = Seq("tataaaggcAATATGCAGTAG") 
print(tatabox_seq.upper())  # TATAAAGGCAATATGCAGTAG 
print(tatabox_seq.lower())  # tataaaggcaatatgcagtag 

