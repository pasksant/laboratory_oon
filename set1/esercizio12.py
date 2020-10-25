def occurrences(str):
 N=0
 for i in range(len(str)):
  if str[i].isalpha():
      N=N+1
 return N
