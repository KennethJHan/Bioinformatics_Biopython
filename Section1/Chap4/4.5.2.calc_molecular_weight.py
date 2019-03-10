# 4.5.2.calc_molecular_weight.py 
from Bio.Seq import Seq 
from Bio.Alphabet import IUPAC 
from Bio.SeqUtils import molecular_weight 

seq1 = Seq("ATGCAGTAG") 
seq2 = Seq("ATGCAGTAG", IUPAC.unambiguous_dna) 
seq3 = Seq("ATGCAGTAG", IUPAC.protein) 

print(molecular_weight(seq1))  # 2842.82 가 출력된다 
print(molecular_weight(seq2))  # 2842.82 가 출력된다 
print(molecular_weight(seq3))  # 707.75 가 출력된다 

