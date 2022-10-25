class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_map = {}
        for l in s: count_map[l] = count_map.get(l, 0) + 1
        
        for (index, l) in enumerate(s):
            if count_map.get(l) == 1: return index
        
        return -1
        