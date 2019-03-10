#13.9.tree.py
from Bio import Phylo
tree = Phylo.read("13.9.nwk","newick")
Phylo.draw(tree, branch_labels = lambda c: c.branch_length)

