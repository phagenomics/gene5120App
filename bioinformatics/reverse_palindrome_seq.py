def reverse_palindrome(seq,length):
  rev_seq = seq[::-1]
  n = length
  for i in range(len(seq)):
    if seq[i:i+n] == rev_seq[i:i+n] and len(seq[i:i+n]) == n:
      return i+1,seq[i:i+n]
