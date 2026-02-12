## GC content calculator
def gc_content(sequence):
    count_a = sequence.count('a')
    count_t = sequence.count('t')
    count_c = sequence.count('c')
    count_g = sequence.count('g')
    return (count_c + count_g) / (count_a + count_t + count_c + count_g)

