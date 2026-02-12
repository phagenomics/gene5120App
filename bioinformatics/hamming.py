def hamming_distance(seq1, seq2):
    """
    Calculate the Hamming distance between two DNA sequences
    of equal length.
    """
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be the same length.")

    distance = 0

    for a, b in zip(seq1.upper(), seq2.upper()):
        if a != b:
            distance += 1

    return distance


# Example usage
dna1 = "GATTACA"
dna2 = "GACTATA"

print("Hamming distance:", hamming_distance(dna1, dna2))
