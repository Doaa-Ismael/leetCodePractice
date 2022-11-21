class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r, maxSum, n = 0, 0, -10000, len(nums)
        
        curSum = 0
        while r < n and l < n:
            curSum += nums[r]
            if curSum >= maxSum: maxSum = curSum
            
            if curSum < 0:
                l, r = r + 1, r + 1
                curSum = 0
            else:
                r += 1
                
        return maxSum
        