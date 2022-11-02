class Solution:
    def isValid(self, s: str) -> bool:
        opened_stack = []
        
        for c in s:
            if c is '(' or c is '{' or c is '[':
                opened_stack.append(c)
            else:
                top = opened_stack.pop() if len(opened_stack) else None
                if not (top == '(' and c == ')' or top == '{' and c == '}'or top == '[' and c == ']'):
                    return False
 
        return True if len(opened_stack) == 0 else False
                
            