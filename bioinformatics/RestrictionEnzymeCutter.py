def restriction(seq, enzyme):
    seq = seq.upper()
    enzyme = enzyme.upper()

    cut_positions = []

    # Find all positions where the enzyme site occurs
    for i in range(len(seq) - len(enzyme) + 1):
        if seq[i:i + len(enzyme)] == enzyme:
            cut_positions.append(i + len(enzyme))  # cut after the site

    # If no cut sites found, return the original sequence
    if not cut_positions:
        return [seq]

    # Generate fragments
    fragments = []
    start = 0

    for cut in cut_positions:
        fragments.append(seq[start:cut])
        start = cut

    fragments.append(seq[start:])  # last fragment

    return fragments