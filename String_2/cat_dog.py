def cat_dog(str):
  count_cat=0
  count_dog=0
  for i in range(len(str)):
      if str[i:i+3]=="cat":
          count_cat+=1
      if str[i:i+4]=="dog":
          count_dog+=1
  return count_cat==count_dog

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))
