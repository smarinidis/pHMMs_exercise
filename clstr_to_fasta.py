#---.clstr to .fasta---
from Bio import SeqIO
import matplotlib.pyplot as plt

# Load representative sequences
rep_seqs = list(SeqIO.parse("C:/Users/stavr/Desktop/clustered_40", "fasta"))
print(f"Unique representative sequences: {len(rep_seqs)}")

# Save them to a new file 2. Conditionals needed
SeqIO.write(rep_seqs, "C:/Users/stavr/Desktop/filtered_unique_sequences.fasta", "fasta")
print("Saved filtered sequences.")

# Parse .clstr to analyze clusters
clusters = []
current = []

with open("C:/Users/stavr/Desktop/clustered_40.clstr") as f:
    for line in f:
        if line.startswith(">Cluster"):
            if current:
                clusters.append(current)
            current = []
        else:
            current.append(line.strip())
    if current:
        clusters.append(current)

# Print summary
cluster_sizes = [len(c) for c in clusters]
print(f"Total clusters: {len(clusters)}")
print(f"Cluster size range: {min(cluster_sizes)} to {max(cluster_sizes)}")

# Optional: plot histogram
plt.hist(cluster_sizes, bins=20, color="skyblue", edgecolor="black")
plt.title("Cluster Size Distribution")
plt.xlabel("Sequences per Cluster")
plt.ylabel("Number of Clusters")
plt.tight_layout()
plt.show()
