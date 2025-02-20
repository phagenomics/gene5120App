#formula being used Tm = 2(A+T) + 4(G+C)

def melting_temp(seq):
    seq=seq.upper()
    tm = 2*(seq.count('A') + seq.count('T')) + 4*(seq.count('G') + seq.count('C'))
    return(tm)
