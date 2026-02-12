
#Given a DNA or RNA sequence, this program will count the number of codons present (set of 3 letters)
#Test DNA Sequence: "ATGCGCTATCAGCATGCGCGCGCGAGAGAGA"
dna_sequence = 
dna_sequence = dna_sequence.replace(" ", "").replace(",", "")
allowed_nucleotides = set('atcguATCGU') # Allow both uppercase and lowercase
if not all(char in allowed_nucleotides for char in dna_sequence):
    raise ValueError("abnormal nucleotide input")
num_codons = len(dna_sequence) // 3
print(f"The number of codons in the sequence is: {num_codons}")
