class Solution:
    def isValid(self, s: str) -> bool:
        opened_stack = []
        mapping = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }
        
        for c in s:
            if mapping.get(c):
                opened_stack.append(mapping[c])
            
            elif not opened_stack or opened_stack.pop() != c:
                return False
 
        return len(opened_stack) == 0
            