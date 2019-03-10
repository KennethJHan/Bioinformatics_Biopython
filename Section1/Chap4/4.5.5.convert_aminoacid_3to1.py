# 4.5.5.convert_aminoacid_3to1.py 
from Bio.SeqUtils import seq3 

essential_amino_acid_1 = "LKMVITWF" 
print(seq3(essential_amino_acid_1))  ## LeuLysMetValIleThrTrpPhe 가 출력된다. 

