def reverse_compliment_seq(seq):
  compliment_lib = str.maketrans({'A':'T','T':'A','C':'G','G':'C'})
  rev_comp_seq = seq.translate(compliment_lib)[::-1]
  return rev_comp_seq

def restriction_site(seq):
  low_range = 4
  high_range = 12
  for n in range(len(seq)-low_range):
    for i in range(low_range, high_range):
      if seq[n:n+i] == reverse_compliment_seq(seq[n:n+i]) and len(seq[n:n+i]) == i:
        print(n+1,len(seq[n:n+i]))