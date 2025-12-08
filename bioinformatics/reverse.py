def reverse_complement(dna_seq):
    bp_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    rev = dna_seq[::-1]
    comp = ''
    for bp in rev:
        comp += bp_dict[bp]
    return comp