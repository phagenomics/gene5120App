
def codon_frequency(input_sequence)
#Given a DNA or RNA sequence, this program will count the number of codons present (set of 3 letters)
#Test DNA Sequence: "ATGCGCTATCAGCATGCGCGCGCGAGAGAGA"
input_sequence = input_sequence.replace(" ", "").replace(",", "")
allowed_nucleotides = set('atcguATCGU') # Allow both uppercase and lowercase
if not all(char in allowed_nucleotides for char in input_sequence):
    raise ValueError("abnormal nucleotide input")
num_codons = len(input_sequence) // 3
print(f"The number of codons in the sequence is: {num_codons}")
