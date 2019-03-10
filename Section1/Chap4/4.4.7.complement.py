# 4.4.7.complement.py 
seq = "TATAAAGGCAATATGCAGTAG" 
comp_dic = { 'A':'T', 'C':'G', 'G':'C', 'T':'A' }  # 상보적 염기를 키-값 으로 하는 사전을 만든다 
comp_seq = "" 
for s in seq:  # 서열에서 하나씩 읽어서 
    comp_seq += comp_dic[s]  # 상보적 염기를 추가해준다 
revcomp_seq = comp_seq[::-1]  # 파이썬 문자열을 뒤집어준다 
print(comp_seq)  # ATATTTCCGTTATACGTCATC 
print(revcomp_seq)  # CTACTGCATATTGCCTTTATA 

