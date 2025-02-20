

def orf_finder(sample):
    def trans(dna):
        return dna.replace('T', 'U')    # Translate DNA to RNA
    code = {
        'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
        'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
        'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
        'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
        'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
        'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
        'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
        'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
        'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}
    rna = trans(sample)
    start_positions = []
    index = 0
    while index < len(rna):
        index = rna.find('AUG', index)
        if index != -1:
            start_positions.append(index)
            index += 1  
        else:
            break
        
    proteins = []
    for start in start_positions:
        protein = []
        count = start
        while count < len(rna):
            codon = rna[count:count + 3]
            amino_acid = code.get(codon, None)
            if amino_acid == 'Stop':
                break
            if amino_acid:  
                protein.append(amino_acid)
                count += 3
        proteins.append(''.join(protein))

    return proteins
