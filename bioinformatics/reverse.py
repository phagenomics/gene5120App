### Janelle's Reverse Complement Tool

def rev_comp(string):
  complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
  reverse_complement = ''.join([complement[base] for base in string[::-1]])
  return reverse_complement
