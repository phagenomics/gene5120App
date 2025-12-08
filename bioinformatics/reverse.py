def rev_comp(string):
    ct_g = string.count('G')
    ct_c = string.count('C')
    length = len(string)
    gc_cont = (ct_g + ct_c) / length
    return gc_cont