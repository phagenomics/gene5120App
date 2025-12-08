# Generates forward and reverse primers from a genomic sequence.

# seq: A string representing the genomic sequence.
#primer_length: An integer representing the desired primer length.
# Returns:
# A tuple containing the forward primer and the reverse primer.
#def primers(sequence):
#    sequence = 'ATGCGGGCGAGCGTTTCGGAGGGTATTTATTATCTTTCTATCATTTTTTAGGGGAGGATTTTAGGGGATTATCTCTCGATCGATTATCGATC'
def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))
def generate_primers(seq, primer_length):
    forward_primer = seq[:primer_length]
    reverse_primer = reverse_complement(seq[-primer_length:])
    return forward_primer, reverse_primer
#Example usage with a primer length of 20:

