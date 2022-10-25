class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = dict()
        for index, num in enumerate(nums):
            other_number = target - num
            if other_number in nums_map:
               return [index, nums_map[other_number]]
            else:
                nums_map[num] = index
    

