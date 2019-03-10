#11.4.5.draw_length_label_tree.py
from Bio import Phylo
tree = Phylo.read("sample_tree4.nwk","newick")
Phylo.draw(tree, branch_labels = lambda c: c.branch_length)

