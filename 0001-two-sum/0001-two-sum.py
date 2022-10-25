class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = dict()
        nums_index = dict()
        for index, num in enumerate(nums):
            value = nums_map.get(num);
            if value is None:
                nums_map[num] = 1
                nums_index[num] = index
            else:
                nums_map[num] = value + 1
                nums_index[num] = index
    
        for index, num in enumerate(nums):
            other_num = target - num
            if other_num in nums_map and num != other_num:
                return [index, nums_index[other_num]]
            elif other_num in nums_map and nums_map[other_num]  > 1:
                return [index, nums_index[other_num]]

