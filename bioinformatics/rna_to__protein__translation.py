# Define the genetic code (codon table)
genetic_code = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',

    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',

    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',

    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def validate_sequence(sequence):
    """Validates if the input sequence contains only valid DNA/RNA characters."""
    valid_dna_chars = set('ATGC')
    valid_rna_chars = set('AUGC')

    if not sequence:
        return False, "Input sequence cannot be empty."

    seq_set = set(sequence.upper())

    is_dna = seq_set.issubset(valid_dna_chars)
    is_rna = seq_set.issubset(valid_rna_chars)

    if is_dna and not is_rna: # Contains 'T' but not 'U'
        return True, "DNA"
    elif is_rna and not is_dna: # Contains 'U' but not 'T'
        return True, "RNA"
    elif is_dna and is_rna: # Contains only A, G, C (could be DNA or RNA)
        # If 'T' is absent, assume RNA as it's the direct translation input
        if 'T' not in seq_set:
            return True, "RNA"
        else:
            return True, "DNA" # Should not happen if 'T' is present and it's also RNA
    else:
        return False, f"Invalid characters found in sequence. Only 'ATGC' or 'AUGC' are allowed. Found: {', '.join(seq_set - valid_dna_chars.union(valid_rna_chars))}"

def transcribe_dna_to_rna(dna_sequence):
    """Transcribes a DNA sequence into an RNA sequence."""
    return dna_sequence.upper().replace('T', 'U')

def translate_rna_to_protein(rna_sequence):
    """Translates an RNA sequence into a protein sequence."""
    protein_sequence = []
    # Ensure sequence length is a multiple of 3
    if len(rna_sequence) % 3 != 0:
        print("Warning: RNA sequence length is not a multiple of 3. Truncating.")
    
    for i in range(0, len(rna_sequence) - len(rna_sequence) % 3, 3):
        codon = rna_sequence[i:i+3]
        amino_acid = genetic_code.get(codon, 'X') # 'X' for unknown/invalid codon
        if amino_acid == '*':
            break # Stop translation at stop codon
        protein_sequence.append(amino_acid)
    return ''.join(protein_sequence)
    



import sys

# --- Main execution block ---
user_sequence = input("Please enter a DNA or RNA sequence: ")

is_valid, seq_type_or_error = validate_sequence(user_sequence)

if not is_valid:
    print(f"Error: {seq_type_or_error}")
    sys.exit()

print(f"Detected sequence type: {seq_type_or_error}")

if seq_type_or_error == "DNA":
    rna_seq = transcribe_dna_to_rna(user_sequence)
    print(f"Transcribed RNA sequence: {rna_seq}")
else:
    rna_seq = user_sequence.upper() # Already RNA

protein_seq = translate_rna_to_protein(rna_seq)

print(f"Predicted Protein sequence: {protein_seq}")