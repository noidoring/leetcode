lst = [1,3,5,6]
targ = 5

def searchInsert(nums, target):
    lst = nums[:]
    lst.append(target)
    lst.sort()
    return lst.index(target)
    

print(searchInsert(lst, targ))

