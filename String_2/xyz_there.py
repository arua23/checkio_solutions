def xyz_there(str):
  if str.find("xyz")!=-1:
      i=str.rindex("xyz")
      return str[i-1]!="."
  return False


print(xyz_there("abc.xxyz"))
print(xyz_there("xyz.abc"))
print(xyz_there("abcxyz"))
print(xyz_there("abc.xyz"))
