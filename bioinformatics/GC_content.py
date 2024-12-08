## GC content calculator
def gc_calc(seq):
    count_c = seq.count('C')
    count_g = seq.count('G')
    count_a = seq.count('A')
    count_t = seq.count('T')
    return (count_c + count_g) / (count_c + count_g + count_a + count_t)

## Primer Design code
def comp(seq):
  chargaff = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
  comp = ' '
  for char in seq:
    comp = comp + chargaff[char]
  return comp[::-1]

def primers(seq):
  fwd = seq[:10:]
  rev = seq[-10:]

  return fwd, comp(rev)

####Calculates the Hamming distance (number of differences) between two DNA sequences.

def hamming_distance(sequence1, sequence2):
  if len(sequence1) != len(sequence2):
    print("Error: These two sequences are of different lengths")
  else:
    total_differences = 0
    for i in range(len(sequence1)):
      if sequence1[i] != sequence2[i]:
        total_differences += 1
    return total_differences 

