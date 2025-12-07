def gc_content(sequence):
    ct_g = sequence.count('G')
    ct_c = sequence.count('C')
    length = len(sequence)
    gc_content = (ct_g + ct_c)/length
    return gc_content
