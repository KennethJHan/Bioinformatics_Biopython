#12.4.KEGG_REST_example.py
from Bio.KEGG import REST

human_pathways = REST.kegg_list("pathway", "hsa").read()

insulin_pathways = []
for line in human_pathways.rstrip().split("\n"):
    entry, description = line.split("\t")
    if "insulin" in description.lower():
        insulin_pathways.append(entry)
        print(entry, description)
print(insulin_pathways)

insulin_genes = []
for pathway in insulin_pathways:
    pathway_file = REST.kegg_get(pathway).read()
    
    current_section = None
    for line in pathway_file.rstrip().split("\n"):
        section = line[:12].strip()
        if not section == "":
            current_section = section
            
            if current_section == "GENE":
                gene_identifiers, gene_description = line[12:].split("; ")
                gene_id, gene_symbol = gene_identifiers.split()
                
                if not gene_symbol in insulin_genes:
                    insulin_genes.append(gene_symbol)
                    
print("There are %d insulin pathways and %d insulin genes. The genes are:" % (len(insulin_pathways), len(insulin_genes)))
print(", ".join(insulin_genes))

