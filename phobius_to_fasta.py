#---phobius(transmembrane part predictions) to fasta file in order to allign them---
from Bio import SeqIO
import re

# SET YOUR FILE PATHS HERE
fasta_file = "C:/Users/stavr/Desktop/uniprotkb_fasta.fasta"
phobius_file = "C:/Users/stavr/Desktop/phobius_fasta.txt"
output_file = "C:/Users/stavr/Desktop/tm_only_sequences.fasta"

# Load FASTA sequences
fasta_seqs = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta-pearson"))  # allow comments

# Open files
with open(output_file, "w") as out_f, open(phobius_file) as pred_f:
    for line in pred_f:
        parts = line.strip().split()
        if len(parts) < 4:
            continue

        full_id = parts[0]  # e.g., sp|A0A0U1RPR8|GUC2D_MOUSE
        seq_id = full_id.replace("|", "")  # GUC2D_MOUSE
        prediction = parts[3]

        # Find TM regions like 123-145, 200-220, etc.
        regions = re.findall(r'(\d+)-(\d+)', prediction)
        if not regions:
            continue

        # Try matching FASTA record
        matched_seq = None
        for key in fasta_seqs:
            if seq_id in key.replace("|", ""):
                matched_seq = fasta_seqs[key]
                break

        if not matched_seq:
            print(f"⚠️ Sequence not found in FASTA: {seq_id}")
            continue

        # Write each TM region as separate sequence
        for i, (start, end) in enumerate(regions, 1):
            start, end = int(start), int(end)
            tm_seq = matched_seq.seq[start-1:end]
            tm_id = f"{seq_id}_TM{i}"
            out_f.write(f">{tm_id}\n{tm_seq}\n")

print("✅ Transmembrane segments saved to:", output_file)
