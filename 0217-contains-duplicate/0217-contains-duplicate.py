class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}
        for num in nums:
            if nums_map.get(num):
                return True
            else:
                nums_map[num] = True
        return False
        