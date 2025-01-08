def searchinsert(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            val = "Element Exists"
        if nums[i-1]< target & target<nums[i]:
            val = i
    return val

nums = [1,3,5,6,9]
target = 5
si = searchinsert(nums, target)
print(si)