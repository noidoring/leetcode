def searchInsert(nums, target):
    lst = nums[:]
    lst.append(target)
    lst.sort()
    return lst.index(target)
    

def searchInsertV2(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = nums[mid]

        if guess <= target:
            return mid - 1
        

nums = [1, 2, 3, 6, 7, 9, 10]
target = 5

print(searchInsertV2(nums, target))