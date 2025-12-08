def transcription(dna_string):
    #replace all Thymine (T) nucleotide bases with Uracil (U)
    rna_string = dna_string.upper().replace("T", "U")
    print(rna_string)
    return TRUE
