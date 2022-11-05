class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_map = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            words_map[tuple(count)].append(s)
    
        return words_map.values()