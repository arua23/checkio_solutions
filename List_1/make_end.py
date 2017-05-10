def make_ends(nums):
  if len(nums)<=1:
      return nums+nums

  return [nums[0],nums[-1]]

print(make_ends([1,2,3]))
print(make_ends([1]))
print(make_ends([1, 2, 3, 4]))
print(make_ends([7, 4, 6, 2]))
print(make_ends([7]))
