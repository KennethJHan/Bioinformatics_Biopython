#11.4.5.draw_length_tree.py
from Bio import Phylo
tree = Phylo.read("sample_tree4.nwk","newick")
Phylo.draw(tree)

