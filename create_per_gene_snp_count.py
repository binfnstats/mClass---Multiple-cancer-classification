import sys
import pandas as pd

df = pd.read_csv(sys.argv[1], sep="\t")
sums = dict(df.sum(axis=0))
x = dict(sums)
with open("gene_snp_frequency.txt", "w") as w:
    for gene in sums:
        if gene != "Cancer_type":
            w.write(gene + "\t" + str(sums[gene]) + "\n")
print("Generated: gene_snp_frequency.txt")
