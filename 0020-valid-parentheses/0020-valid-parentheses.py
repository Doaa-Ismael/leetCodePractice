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
            
            elif not len(opened_stack) or opened_stack.pop() != c:
                return False
 
        return True if len(opened_stack) == 0 else False
                
            