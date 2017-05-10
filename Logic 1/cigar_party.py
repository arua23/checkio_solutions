def cigar_party(cigars, is_weekend):
  if is_weekend==True and cigars>=40:
      return True
  else:
      if is_weekend==False and (cigars>=40 and cigars<=60):
          return True
  return False


print(cigar_party(60,False))
print(cigar_party(30, False))
print(cigar_party(50,False))
print(cigar_party(70,True))
