def array_front9(nums):
  l=len(nums)
  if l<4:
      if 9 in nums:
          return True
      else:
          return False
  if l>=4:
      if 9 in nums[0:4]:
          return True
      else:
          return False
        
print(array_front9([1,9,4]))     
print(array_front9([1,2,4,5,9]))
print(array_front9([1,9,4,5,9]))
print(array_front9([1,2,4,9,9]))
print(array_front9([1,2,4,7,9,9]))

##nums=[1,2,3,4,5,9]
##if 9 in nums[0:4]:
##    print("Boo Yeah")
##else:
##    print("Damn")
