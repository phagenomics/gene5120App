#using strip to remove spaces, first bug  
def gc_content(sequence1):
    gcontent = sequence1.strip().count('G')
    ccontent = sequence1.strip().count('C')
    gc_content = (gcontent + ccontent)/len(sequence1.strip())
    return gc_content

sequence1 = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

gc_content(sequence1)