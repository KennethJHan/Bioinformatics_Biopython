# 4.5.5.convert_aminoacid_1to3.py 
from Bio.SeqUtils import seq1 

essential_amino_acid_3 = "LeuLysMetValIleThrTrpPhe" 
print(seq1(essential_amino_acid_3))  ## LKMVITWF 가 출력된다. 

