class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for c in s:
            if c == '#' and len(s_stack):
                s_stack.pop()
            elif c == '#':
                continue;
            else:
                s_stack.append(c)
        for c in t:
            if c == '#' and len(t_stack):
                t_stack.pop()
            elif c == '#':
                continue;
            else:
                t_stack.append(c)
        return ''.join(s_stack) == ''.join(t_stack)
                
    