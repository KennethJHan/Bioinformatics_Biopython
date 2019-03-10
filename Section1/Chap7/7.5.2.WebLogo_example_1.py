#7.5.2.WebLogo_example_1.py 

from Bio.motifs import Motif 
from Bio import motifs 
from Bio.Seq import Seq 

instances = [Seq("TACAA"), 
            Seq("TACGC"), 
            Seq("TACAC"), 
            Seq("TACCC"), 
            Seq("AACCC"), 
            Seq("AATGC"), 
            Seq("AATGC"), 
            ] 

m = motifs.create(instances) 

print(m.counts)
Motif.weblogo(m,'test.png')
