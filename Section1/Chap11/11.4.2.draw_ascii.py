#11.4.2.draw_ascii.py
## ASCII 형태로 tree 객체 출력하기
from Bio import Phylo
tree = Phylo.read("sample_tree3.nwk","newick")
Phylo.draw_ascii(tree)

