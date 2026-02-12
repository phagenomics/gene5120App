def transcription(dna_string):
  
    dna_string = dna_string.upper()
    valid_bases = {'A', 'T', 'G', 'C'}
    if not all(base in valid_bases for base in dna_string):
        invalid_chars = set(char for char in dna_string if char not in valid_bases)
        raise ValueError(f"Invalid character(s) found in DNA sequence: {', '.join(invalid_chars)}. Only A, T, G, C are allowed.")

    rna_sequence = dna_string.replace('A', 'U')
    return rna_sequence 

#I tested on colab, added a line to ensure that only A T C G are allowed in the imput other wise
# it will retun invalid error

#Converted all A -> U to go from DNA to RNA