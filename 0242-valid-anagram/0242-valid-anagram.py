class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map = {}, {}
        for l in s: s_map[l] = s_map.get(l, 0) + 1
        for l in t: t_map[l] = t_map.get(l, 0) + 1
        
        return s_map == t_map
      
        