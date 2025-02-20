def gc_content(sequence1):
    gcontent = sequence1.count('G')
    ccontent = sequence1.count('C')
    gc_content = (gcontent + ccontent)/len(sequence1)
    return gc_content

sequence1 = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

gc_content(sequence1)
