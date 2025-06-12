#Script for finding the unique sequencies between two files
def read_fasta_ids(file_path):
    ids = set()
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('>'):
                ids.add(line.strip())
    return ids

def extract_unique_entries(full_file, subset_file, output_file):
    subset_ids = read_fasta_ids(subset_file)

    with open(full_file, 'r') as f_in, open(output_file, 'w') as f_out:
        write_entry = False
        for line in f_in:
            if line.startswith('>'):
                if line.strip() not in subset_ids:
                    write_entry = True
                    f_out.write(line)
                else:
                    write_entry = False
            elif write_entry:
                f_out.write(line)

# Example usage
full_fasta = 'C:/Users/stavr/Desktop/uniprotkb_fasta.fasta'      # Replace with your main FASTA file
subset_fasta = 'C:/Users/stavr/Desktop/filtered_unique_sequences.fasta'  # Replace with the subset FASTA file
output_fasta = 'C:/Users/stavr/Desktop/unique_entries.fasta'

extract_unique_entries(full_fasta, subset_fasta, output_fasta)
print("Unique entries written to:", output_fasta)
