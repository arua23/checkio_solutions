def sum13(nums):
  if nums.count(13)==0:
      return sum(nums)
  else:
    c=nums.count(13)
    while c!=0:
      


print(sum13([1,2,2,1]))
print(sum13([1,1]))
print(sum13([1,2,2,13,13]))
