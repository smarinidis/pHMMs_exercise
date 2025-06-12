#Script for counting
def count_fasta_entries(file_path):
    count = 0
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('>'):
                count += 1
    return count

# Example usage
fasta_file = 'C:/Users/stavr/Desktop/positive_check.fasta'  # Replace with your file path
num_entries = count_fasta_entries(fasta_file)
print(f"Number of protein sequences: {num_entries}")
