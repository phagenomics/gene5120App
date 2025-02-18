# bioinformatics_tools.py
import re

# Reverse Complement
def reverse_comp(sequence):
    complement = str.maketrans("ATGC", "TACG")
    return sequence.translate(complement)[::-1]  # Reverse after complement

# GC Content Calculation
def gc_content(sequence):
    gc_count = sum(1 for base in sequence if base in "GC")
    return (gc_count / len(sequence)) * 100 if sequence else 0

# Transcription (DNA to RNA)
def transcription(sequence):
    return sequence.replace("T", "U")

# Codon Frequency Calculation
def codon_frequency(sequence):
    codons = [sequence[i:i+3] for i in range(0, len(sequence) - 2, 3)]
    freq = {codon: codons.count(codon) for codon in set(codons)}
    return freq

# Translation (DNA to Protein)
codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'STOP', 'TAG':'STOP',
    'TGC':'C', 'TGT':'C', 'TGA':'STOP', 'TGG':'W'
}
def translation(sequence):
    return ''.join(codon_table.get(sequence[i:i+3], '?') for i in range(0, len(sequence) - 2, 3))

# Hamming Distance
def hamming(seq1, seq2):
    if len(seq1) != len(seq2):
        return "Sequences must be the same length."
    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))

# Melting Temperature (Basic)
def melting_temp(sequence):
    return (sequence.count('A') + sequence.count('T')) * 2 + (sequence.count('G') + sequence.count('C')) * 4

# Restriction Enzyme Recognition
def restriction(sequence, recognition_site):
    return [m.start() for m in re.finditer(recognition_site, sequence)]

# Find Palindromic Sequences
def palindrome(sequence, length):
    return [sequence[i:i+length] for i in range(len(sequence) - length + 1) if sequence[i:i+length] == sequence[i:i+length][::-1]]

# ORF Finder
def orf_finder(sequence):
    orfs = []
    for i in range(3):  # Three reading frames
        for j in range(i, len(sequence)-2, 3):
            codon = sequence[j:j+3]
            if codon == "ATG":
                for k in range(j, len(sequence)-2, 3):
                    stop_codon = sequence[k:k+3]
                    if stop_codon in ["TAA", "TAG", "TGA"]:
                        orfs.append(sequence[j:k+3])
                        break
    return orfs

# Primer Design (Generate forward and reverse primers)
def primers(sequence, length):
    if length > len(sequence):
        return "Primer length exceeds sequence length"
    forward = sequence[:length]
    reverse = reverse_comp(sequence[-length:])
    return {"forward": forward, "reverse": reverse}

# Atomic Mass Calculation
mass_table = {
    'A': 135.13, 'T': 126.11, 'G': 151.13, 'C': 111.10
}
def atomic_mass(sequence):
    return sum(mass_table.get(base, 0) for base in sequence)
