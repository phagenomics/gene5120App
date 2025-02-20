#Cleaning 2 Bugs 
def gc_content(sequence1):
    gcontent = sequence1.strip().count('G')
    ccontent = sequence1.strip().count('C')
    acontent = sequence1.strip().count('A')
    tcontent = sequence1.strip().count('T')
    gc_content = (gcontent + ccontent)/(gcontent + ccontent + acontent + tcontent)
    return gc_content

sequence1 = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

gc_content(sequence1)