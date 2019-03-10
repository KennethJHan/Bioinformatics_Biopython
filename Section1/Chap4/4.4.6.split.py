# 4.4.6.split.py 
from Bio.Seq import Seq 

mrna = Seq("AUGAACUAAGUUUAGAAU") 
ptn = mrna.translate() 
print(ptn)  ## MN*V*N 
for seq in ptn.split("*"): 
    print(seq) 

