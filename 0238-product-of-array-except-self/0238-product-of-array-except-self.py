class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf, ans = nums[::], nums[::], []
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i]
            
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] * nums[i]
            
            
        for i in range(0, len(nums)):
            if i == 0:
                nums[i] = suf[i+1]
            elif i == len(nums) - 1:
                nums[i] = pre[i-1]
            else:
                 nums[i] = pre[i-1] * suf[i+1]
        return nums
        