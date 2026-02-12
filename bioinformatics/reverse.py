## This will be a quick
def rev_comp(dna_seq):
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
## Will take the sequence given, match it to the reverse base and join the bases together to form the sequence
    rev_comp = ''.join(complement.get(base, base) for base in reversed(dna_seq))
    
    return rev_comp
