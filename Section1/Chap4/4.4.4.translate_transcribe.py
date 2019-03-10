# 4.4.4.translate_transcribe.py 

from Bio.Seq import Seq 

dna = Seq("ATGCAGTAG") 
mrna = dna.transcribe() 
ptn = dna.translate() 
print(mrna)  # AUGCAGUAG 
print(ptn)  # MQ* 

