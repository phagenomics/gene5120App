def dna_to_rna(dna_sequence):
  
    dna_sequence = dna_sequence.upper()
    valid_bases = {'A', 'T', 'G', 'C'}
    if not all(base in valid_bases for base in dna_sequence):
        invalid_chars = set(char for char in dna_sequence if char not in valid_bases)
        raise ValueError(f"Invalid character(s) found in DNA sequence: {', '.join(invalid_chars)}. Only A, T, G, C are allowed.")

    rna_sequence = dna_sequence.replace('A', 'U')
    return rna_sequence 