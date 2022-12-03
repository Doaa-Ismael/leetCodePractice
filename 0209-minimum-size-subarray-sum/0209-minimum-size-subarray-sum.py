class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, n, ans = 0, 0, len(nums), inf
        curSum = 0
        
        while True:
            if curSum >= target:
                if l >= n: break
                curSum -= nums[l]
                l += 1
                r = r if r >=l else l
            else:
                if r >= n: break
                curSum += nums[r]
                r += 1
            if curSum >= target:
                ans = min(ans, r-l)
     
            
        return ans if ans != inf else 0
            
            
        