# Generates forward and reverse primers from a genomic sequence.

# seq: A string representing the genomic sequence.
#primer_length: An integer representing the desired primer length.
# Returns:
# A tuple containing the forward primer and the reverse primer.
#def primers(sequence):
#    sequence = 'ATGCGGGCGAGCGTTTCGGAGGGTATTTATTATCTTTCTATCATTTTTTAGGGGAGGATTTTAGGGGATTATCTCTCGATCGATTATCGATC'

def primers(seq, primer_length):
    forward = seq[:primer_length]
    complement = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    
    reverse = ''.join(
        complement[base] for base in reversed(seq[-primer_length:])
    )

    return forward, reverse
