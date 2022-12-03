class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, n, ans = 0, 0, len(nums), inf
        curSum = 0
        
        for r in range(0, len(nums)):
            curSum += nums[r]
            while curSum >= target:
                ans = min(ans, r-l+1)
                curSum -= nums[l]
                l += 1
     
            
        return ans if ans != inf else 0
            
            
        