def reverse_palindrome(seq,length):
  results = []
  n= len(seq)

  def reverse_compliment(seq):
        complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        complement_seq = "".join([complement_map[base] for base in seq])
        return complement_seq[::-1]

  for i in range(n):
        for j in range(i), min(i + 1, n + 1):
            substring = seq[i:j]
            return substring

#reverse_palindrome(Rosalind_4746, 4, 12)
