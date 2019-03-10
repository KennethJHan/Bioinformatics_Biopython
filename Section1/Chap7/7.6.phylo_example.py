#7.6.phylo_example.py 

from Bio import Phylo 

tree = Phylo.read('HBA.newick', 'newick') 
print(tree) 

Phylo.draw(tree) 

