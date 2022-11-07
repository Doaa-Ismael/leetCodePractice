class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getString(string: str) -> str:
            count, ans = 0, ''
            n = len(string)
            for i in range(n):
                if string[n-i-1] == '#':
                    count -= 1
                else:
                    if count < 0:
                        count += 1
                    else:
                        ans += string[n-i-1]
            return ans


        return getString(s) == getString(t)
                
    