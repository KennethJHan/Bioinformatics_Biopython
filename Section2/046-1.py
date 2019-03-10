#046-1.py

seq = "11A2TG3TT000AT1A2G"
new_seq = ""

for s in seq:
    if s.isalpha():
        new_seq += s
        
print(new_seq)

