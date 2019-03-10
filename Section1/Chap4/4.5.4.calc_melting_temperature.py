# 4.5.4.calc_melting_temperature.py 
from Bio.SeqUtils import MeltingTemp as mt 
from Bio.Seq import Seq 

myseq = Seq("AGTCTGGGACGGCGCGGCAATCGCA") 
print(mt.Tm_Wallace(myseq))  # 84.0 이 출력된다. 

