def melting_temp(sequence):
    i=0
    w=0
    x=0
    y=0
    z=0
    for aa in sequence:
        if aa == 'A':
            w += 1
        elif aa == 'T':
            x += 1
        elif aa == 'G':
            y +=1
        else:
            z += 1

    if len(sequence) <= 14:
        Tm = (w+x)*2 + (y +z)*4
    else:
        Tm = 64.9 +41*(y+z-16.4)/(w+x+y+z)
    return Tm

#I'm following along