def reverse_comp(sequence):
    complement = ''
    comp = {
        'T': 'A', 'C': 'G', 'A': 'T', 'G': 'C'
    }
    for nucleotide in sequence:
        complement += comp.get(nucleotide, 'N')  # Handle unexpected characters
    return complement[::-1]
