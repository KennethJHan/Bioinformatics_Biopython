#11.4.4.draw_color_tree.py
from Bio import Phylo
tree = Phylo.read("sample_tree3.nwk","newick")
tree.rooted = True
tree.root.color = (128,128,128)
print(tree)
print("tree.clade[0]:", tree.clade[1])
print("tree.clade[1]:", tree.clade[1])
print("tree.clade[2,0]:", tree.clade[2,0])
print("tree.clade[2,1]:", tree.clade[2,1])
tree.clade[1].color = "blue"
tree.clade[2,0].color = "red"
Phylo.draw(tree)

