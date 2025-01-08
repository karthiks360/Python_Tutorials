# Works only for ordered array

def removeduplicates(nums):
    arr = []
    for i in range(len(nums)):
        if nums[i-1] != nums[i]:
            arr.append(nums[i])
    
    return arr

nums = [0,0,1,1,1,2,2,3,3,4,4,5,6,7,7,7,8,8,8]
rd = removeduplicates(nums)
print(rd)