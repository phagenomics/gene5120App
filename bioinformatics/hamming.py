def hamming(s,t): #takes in two strings
    if len(s) != len(t):
        raise ValueError
    mutations = 0
    for i in range(len(seq1)):
     if seq1[i] != seq2[i]:
      mutations += 1
    return True