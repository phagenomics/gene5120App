### Janelle's Reverse Complement Tool
## add 'strip' to remove trailing spaces
## skip unknown bases

def rev_comp(string):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    string = string.strip()
    reverse_complement = ''.join([complement.get(base, '') for base in string[::-1]])
    return reverse_complement
