def reverse_complement(dna_seq):
    complement = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
        'a': 't',
        't': 'a',
        'c': 'g',
        'g': 'c'
    }
    
    rev_comp = ''.join(complement.get(base, base) for base in reversed(dna_seq))
    
    return rev_comp

print(reverse_complement(sequence))
