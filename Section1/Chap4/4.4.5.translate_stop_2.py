# 4.4.5.translate_stop_2.py 
from Bio.Seq import Seq 

mRNA = Seq("AUGAACUAAGUUUAGAAU") 
ptn = mRNA.translate(to_stop=True) 
print(ptn) ## MN 

