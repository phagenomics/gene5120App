test = 'TCAATGCATGCGGGTCTATATGCAT'

def reverse_palindrome(seq,length):
  compliment_lib = str.maketrans({'A':'T','T':'A','C':'G','G':'C'})
  rev_comp_seq = seq.translate(compliment_lib)[::-1]
  n = length
  for i in range(len(seq)):
    if seq[i:i+n] == rev_comp_seq[i:i+n]:
      print(n+1,(seq[i:i+n]))

reverse_palindrome(test, 4)