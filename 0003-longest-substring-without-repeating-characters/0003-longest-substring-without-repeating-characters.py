class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, ans, n = 0, 0, 0, len(s)
        chars = set()
        while l<n and r <n:
            char = s[r]
            if char in chars:
                chars.remove(s[l])
                l += 1
            else:
                chars.add(char)
                r += 1
            ans = max(ans, len(chars))
        return ans
    