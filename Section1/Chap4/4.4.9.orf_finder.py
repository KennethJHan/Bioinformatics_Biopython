# 4.4.9.orf_finder.py

from Bio.Seq import Seq

tatabox_seq = Seq("tataaaggcAATATGCAGTAG")
start_idx = tatabox_seq.find("ATG")   
end_idx = tatabox_seq.find("TAG", start_idx)  # 예문의 편의상 TAG 로 하였다.  
orf = tatabox_seq[start_idx:end_idx+3]  # 파이썬 문자열과 같은 방법으로 슬라이싱이 가능하다. 
print(orf)  # ATGCAGTAG

