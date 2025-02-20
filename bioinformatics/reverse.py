### Janelle's Reverse Complement Tool
## add 'strip' to remove trailing spaces

def rev_comp(string):
  complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
  string = string.strip()
  reverse_complement = ''.join([complement[base] for base in string[::-1]])
  return reverse_complement

