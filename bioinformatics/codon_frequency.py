# Codon Frequency Calculator
# Input a DNA or RNA and count the number of codons

# Test string
STRING = "ATGAGTAGCTACGTAGCTAGCTAGCTAGCTAGCTGATCGATCGTACGTAGCTAGCTAGCTGATCGATCGTACGTACGTCAGCTAG"
# STRING = "AUGUAGUAUCGUACGUAGCUAGCUAGCUAGCUAGCUAGCUGAUCGAUCGUACGUACGUCGAUGCUAGCUAGCUAGCUAGCUAGCUGA"


def to_rna(sequence):
    """
    Converts DNA sequence to RNA
    """
    return sequence.replace("T", "U")

# Find codons

def show_codons(sequence):
    """
    Requires to_rna(). Given an RNA sequence, counts how many codons there are. 
    """
    codon_table = {
        'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
        'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
        'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
        'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
        'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
        'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
        'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
        'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
        'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
        'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
        'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
        'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
        'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
        'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
        'UGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
        'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G', 
        }
    
    total_codons = 0

    input_rna = to_rna(sequence)
    n = 3 #for number of nucleotides per codon
    for i in range(len(input_rna)):

        if input_rna[i:i+n] == "AUG": # Finds start codon
            # Only keeps codons with length of n declared
            codons = [input_rna[j:j+n] for j in range(i, len(input_rna), n) if len(input_rna[j:j+n]) == n]
            

            for codon in codons:  
                    if codon in codon_table:
                        if codon_table[codon] == 'Stop':
                            total_codons += 1
                            break
                        else:
                            total_codons += 1

            # # Final check to make sure the last codon is a Stop codon and not just the end of the string
            # if codon_table[codon] == "Stop": 
            #     proteins.append(protein) 
    # return total_codons
    return codons


def codon_frequency(input_sequence):
    if "T" in input_sequence:
        input_rna = to_rna(input_sequence)
    else: 
        input_rna = input_sequence
    codons = show_codons(input_rna)
    dictionary = {i:codons.count(i) for i in set(codons)}
    # # return show_codons(input_rna)
    return dictionary





# print(f"There is a start codon.\nTotal number of valid codons: {codon_frequency(STRING)}")
    


