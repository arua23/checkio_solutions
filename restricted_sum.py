def res_sum(nums,tmp,x):
    tmp+=nums[x]
    if not(x<len(nums)-1):
        return tmp
    else:
        return res_sum(nums,tmp,x+1)
        

def checkio(data):
    total=res_sum(data,0,0)
    return total

print(checkio([2,2,2,2,2]))
print(checkio([1,2,3,4]))

