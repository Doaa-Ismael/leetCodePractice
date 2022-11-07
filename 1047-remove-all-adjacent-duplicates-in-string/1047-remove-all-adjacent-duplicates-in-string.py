class Solution:
    def removeDuplicates(self, s: str) -> str:
        s_stack = []
        for c in s:
            if len(s_stack) and s_stack[-1] == c:
                s_stack.pop()
            else:
                s_stack.append(c)
                
        return ''.join(s_stack)
                