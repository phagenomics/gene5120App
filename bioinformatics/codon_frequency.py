
#Given a DNA or RNA sequence, this program will count the number of codons present (set of 3 letters)
#Test DNA Sequence: "ATGCGCTATCAGCATGCGCGCGCGAGAGAGA"
#input_sequence = "ATGCGCTATCAGCATGCGCGCGCGAGAGAGA"



def codon_frequency(input_sequence):
    processed_sequence = input_sequence.replace(" ", "").replace(",", "").replace(".", "")
    allowed_nucleotides = set('atcguATCGU')
    if not all(char in allowed_nucleotides for char in processed_sequence):
        raise ValueError("abnormal nucleotide input")

    processed_sequence = processed_sequence.upper()

    nucleotide_counts = Counter(processed_sequence)
    return nucleotide_counts

nucleotide_frequencies = codon_frequency(input_sequence)
nucleotide_frequencies