def centered_average(nums):
  nums.sort()
  nums.remove(nums[0])
  nums.remove(nums[-1])
  s=sum(nums)
  return s//len(nums)



print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))
