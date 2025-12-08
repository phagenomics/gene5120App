def restriction(seq, enzyme):
    seq = seq.upper()
    site = enzyme['site'].upper()
    cut_offset = enzyme['cut_offset']

    cut_positions = []
    start = 0

     # Find all occurrences of recognition site
    while True:
        pos = seq.find(site, start)
        if pos == -1:
            break
        cut_positions.append(pos + cut_offset)
        start = pos + 1

    if not cut_positions:
        return [seq] 
    # No cuts
    fragments = []
    previous = 0
    for cut in cut_positions:
        fragments.append(seq[previous:cut])
        previous = cut
    fragments.append(seq[previous:])
    return fragments
