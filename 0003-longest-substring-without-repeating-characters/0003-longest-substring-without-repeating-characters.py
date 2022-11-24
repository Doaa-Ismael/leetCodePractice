class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, ans, n = 0, 0, 0, len(s)
        charsMap = {}
        
        for r in range(n):
            if s[r] in charsMap:
                l = max(charsMap[s[r]] + 1, l)
                
            charsMap[s[r]] = r
            ans = max(ans, r-l+1)
        return ans
    