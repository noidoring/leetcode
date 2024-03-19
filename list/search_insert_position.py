def searchInsert(nums, target):
    lst = nums[:]
    lst.append(target)
    lst.sort()
    return lst.index(target)
    