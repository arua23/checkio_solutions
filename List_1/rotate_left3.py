def rotate_left3(nums):
    r=nums[-2::]+nums[-3::-1]
    return r

print(rotate_left3([1,2,3]))
print(rotate_left3([5, 11, 9]))
print(rotate_left3([7, 0, 0]))
    
  
