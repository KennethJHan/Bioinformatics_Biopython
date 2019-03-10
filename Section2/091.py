#091.py

A, C, G, T = 0, 0, 0, 0

with open("sample1.fasta","r") as fr:
    for line in fr:
        if line.startswith(">"):
            pass
        else:
            A += line.count("A")
            C += line.count("C")
            G += line.count("G")
            T += line.count("T")
            
print("A", A)
print("C", C)
print("G", G)
print("T", T)
                
