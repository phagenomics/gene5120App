def restriction(seq, enzyme):
    seq = seq.upper()
    site = enzyme['site'].upper()
    cut_pos = enzyme['cut_pos'0]
    cut_pos1 = enzyme.get("cut_pos1", none)
    if cut_pos1 is None:
        cut_pos1 = cut_pos
    return TRUE