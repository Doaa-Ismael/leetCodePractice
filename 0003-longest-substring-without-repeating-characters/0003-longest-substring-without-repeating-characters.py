class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, ans, n, curLen = 0, 0, 0, len(s), 0
        chars = set()
        while l<n and r<n:
            char = s[r]
            if char in chars:
                ans = max(ans, curLen)
                chars.clear()
                l = r = l+1
                curLen = 0
            else:
                chars.add(char)
                curLen += 1
                r += 1
            ans = max(ans, curLen)
        return ans