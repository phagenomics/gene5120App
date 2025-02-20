#s= "AGCTCGTCGACGTAC"
#t= "GCTACGTACGTACCT"

def hamming_tool(s,t): #takes in two strings
  s = s.strip()
  t = t.strip()
  if len(s)==len(t): #checks for lengths
    HamCount =0 #init var
    for i in range(len(s)): #iterate through list
      if s[i]!=t[i]: #if they dont match, increase counter
        HamCount +=1
    return HamCount #return counter
  else:
    print("Strings are not equal")