def removeElement(nums, val):
        arr = []
        for i in range (len(nums)):
            if nums[i] != val:
                arr.append(nums[i]) 
        return arr  

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
k = removeElement(nums, val)
print(k)