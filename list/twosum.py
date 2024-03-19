class Solution:
    def twoSum(self, nums, target):
        for first_index, number in enumerate(nums):
            for second_index, second_number in enumerate(nums):
                if first_index == second_index:
                    continue
                if number + second_number == target:
                    return [first_index, second_index]