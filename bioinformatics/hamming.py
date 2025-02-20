# s= "A1GCTCGTCGACGTAC"
# t= "GCTACGTACGTACCTC"

def hamming(s,t): #takes in two strings
  s = s.strip()
  t = t.strip()
  if len(s)==len(t): #checks for lengths
    HamCount =0 #init var
    for i in range(len(s)): #iterate through list
      if s[i] != 'A' or 'C' or 'T' or 'G':
        return('Number detected in string')
        break
      elif t[i] != 'A' or 'C' or 'T' or 'G':
        return('Number detected in string')
        break
      elif s[i]!=t[i]: #if they dont match, increase counter
        HamCount +=1
    return HamCount #return counter
  else:
    return("Strings are not equal") 