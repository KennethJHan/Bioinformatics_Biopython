#11.4.1.read_newick.py
from Bio import Phylo
tree = Phylo.read("sample_tree3.nwk","newick")
print(type(tree))
print(tree)

