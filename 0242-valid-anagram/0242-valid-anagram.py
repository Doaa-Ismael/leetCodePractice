class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1 = {}
        m2 = {}
        for l in s:
            m1[l] = m1.get(l) + 1 if m1.get(l) is not None else 1 
        for l in t:
            m2[l] = m2.get(l) + 1 if m2.get(l) is not None else 1
        
        if len(m1) != len(m2):
            return False
        
        for c in m1:
            if m1.get(c) != m2.get(c):
                return False
        return True
        
        