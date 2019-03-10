#13.5.WebLogo.py

from Bio.motifs import Motif 
from Bio import motifs 
from Bio.Seq import Seq 

instances = [Seq("AATTAAA"), 
             Seq("AAAAAGA"), 
             Seq("AAATAGC"), 
             Seq("AATCAAC"), 
             Seq("AATTTAA"), 
             Seq("TATCAGA"), 
             Seq("ATATAGC"), 
             Seq("ATATTAA"), 
            ] 

m = motifs.create(instances) 

print(m.counts)
Motif.weblogo(m,'13.5.png')
