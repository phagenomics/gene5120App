codon_table = {
    'GCU' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A',
    'UGU' : 'C', 'UGC' : 'C',
    'GAU' : 'D', 'GAC' : 'D',
    'GAA' : 'E', 'GAG' : 'E',
    'UUU' : 'F', 'UUC' : 'F',
    'GGU' : 'G', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G',
    'CAU' : 'H', 'CAC' : 'H',
    'AUA' : 'I', 'AUC' : 'I', 'AUU' : 'I',
    'AAA' : 'K', 'AAG' : 'K',
    'UUA' : 'L', 'UUG' : 'L', 'CUU' : 'L', 'CUC' : 'L', 'CUA' : 'L', 'CUG' : 'L',
    'AUG' : 'M',
    'AAU' : 'N', 'AAC' : 'N',
    'CCU' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P',
    'CAA' : 'Q', 'CAG' : 'Q',
    'CGU' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R', 'AGA' : 'R', 'AGG' : 'R',
    'UCU' : 'S', 'UCC' : 'S', 'UCA' : 'S', 'UCG' : 'S', 'AGU' : 'S', 'AGC' : 'S',
    'ACU' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T',
    'GUU' : 'V', 'GUC' : 'V', 'GUA' : 'V', 'GUG' : 'V',
    'UGG' : 'W',
    'UAU' : 'Y', 'UAC' : 'Y',
    'UAA' : 'Stop', 'UAG' : 'Stop', 'UGA' : 'Stop',
}

def translation(rna):
    protein_seq = ''
    start = rna.find('AUG')
    for i in range(start, len(rna), 3):
        codon = rna[i:i+3]
        if codon in codon_table:
            amino_acid = codon_table[codon]
            if amino_acid == 'Stop':
                break
            protein_seq += amino_acid
    return protein_seq

    



