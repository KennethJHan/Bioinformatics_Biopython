#12.3.KEGG_Enzyme_example.py

from Bio.KEGG import Enzyme

records = Enzyme.parse(open("ec_2.7.1.40.txt"))
record = list(records)[0]
print("classname:", record.classname)
print("sysname:", record.sysname)
print("subtrate:", record.substrate)
print("product:", record.product)

