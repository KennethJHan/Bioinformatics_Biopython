#13.10.KEGG.py
from Bio.KEGG import REST

human_pathways = REST.kegg_list("pathway", "hsa").read()

hepatitis_pathways = []
for line in human_pathways.rstrip().split("\n"):
    entry, description = line.split("\t")
    if "hepatitis" in description.lower():
        hepatitis_pathways.append(entry)
        print(entry, description)
print(hepatitis_pathways)

hepatitis_genes = []
for pathway in hepatitis_pathways:
    pathway_file = REST.kegg_get(pathway).read()
    
    current_section = None
    for line in pathway_file.rstrip().split("\n"):
        section = line[:12].strip()
        if not section == "":
            current_section = section
            
            if current_section == "GENE":
                gene_identifiers, gene_description = line[12:].split("; ")
                gene_id, gene_symbol = gene_identifiers.split()
                
                if not gene_symbol in hepatitis_genes:
                    hepatitis_genes.append(gene_symbol)
                    
print("There are %d hepatitis pathways and %d hepatitis genes. The genes are:" % (len(hepatitis_pathways), len(hepatitis_genes)))
print(", ".join(hepatitis_genes))
