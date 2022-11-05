class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_map = {}
        for s in strs:
            soerted_word = ''.join(sorted(s))
            if words_map.get(soerted_word):
                words_map.get(soerted_word).append(s)
            else:
                words_map[soerted_word] = [s]

        return words_map.values()