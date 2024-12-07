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
