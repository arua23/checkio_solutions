def string_splosion(str):
  i=len(str)
  j=0
  out_str=""
  while i!=-1:
      out_str=out_str+str[0:j]
      j+=1
      i-=1
  return out_str

print(string_splosion("code"))
print(string_splosion("abc"))
print(string_splosion('ab'))
