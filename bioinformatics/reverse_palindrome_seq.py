#Sequence palindrome finder
def reverse_complement(seq):
    complement = {'A':'T','T':'A','C':'G','G':'C'}
    seq = seq.upper()
    return "".join(complement[base] for base in reversed(seq))

def find_palindromes_window(sequence, min_len=4, max_len=12):
    sequence = sequence.upper()
    results = []

    for length in range(min_len, max_len + 1):
        for i in range(len(sequence) - length + 1):
            subseq = sequence[i:i+length]
            rev_comp = reverse_complement(subseq)
            if subseq == rev_comp:
                results.append((i, i+length, subseq))

    return results

#Example
#seq = "ATGCCGATGCGTGTGTCGCGCAATA"
#palindromes = find_palindromes_window(seq, min_len=4, max_len=12)
#for _, _, pal in palindromes:
#    print(pal)

#Upload to GitHub
