#13.2.fasta_record_counter.py

from Bio import SeqIO

f = "13.2.fasta"

with open(f,"rU") as handle:
    for record in SeqIO.parse(handle,"fasta"):
        seq = record.seq
        print(record.id)
        print("A",seq.upper().count("A"))
        print("C",seq.upper().count("C"))
        print("G",seq.upper().count("G"))
        print("T",seq.upper().count("T"))
        print("N",seq.upper().count("N"))
