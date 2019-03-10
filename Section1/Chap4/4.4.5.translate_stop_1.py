# 4.4.5.translate_stop_1.py 
from Bio.Seq import Seq 

mRNA = Seq("AUGAACUAAGUUUAGAAU") 
ptn = mRNA.translate() 
print(ptn)  ## MN*V*N 

