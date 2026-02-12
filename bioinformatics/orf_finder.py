def orf(sequence):
  stop_codons = {"UAA", "UAG", "UGA"}
  orfs = []

  for frame in range(3):  
      for i in range(frame, len(sequence) - 2, 3):
          codon = sequence[i:i+3]
          
          if codon == "AUG":
              for j in range(i+3, len(sequence) - 2, 3):
                  stop = sequence[j:j+3]
                  
                  if stop in stop_codons:
                      orf = sequence[i:j+3]
                      orfs.append({
                          "frame": frame,
                          "start": i,
                          "end": j+3,
                          "length": len(orf),
                          "sequence": orf
                      })
                      break
  orf_sequences = [o["sequence"] for o in orfs]
  return print(orf_sequences)

