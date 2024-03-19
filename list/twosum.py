class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_index, number in enumerate(nums):
            for second_index, second_number in enumerate(nums):
                if first_index == second_index:
                    continue
                if number + second_number == target:
                    return [first_index, second_index]