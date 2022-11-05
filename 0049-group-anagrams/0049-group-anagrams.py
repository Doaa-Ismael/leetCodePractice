class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # sort them n * n*lg(n) n
    # ["eat","tea","tan","ate","nat","bat"]
    # ["eat","eat","tan","eat","tan","bat"]
    # I will form them in a set
    # ["eat": [], "tan": [], "bat": []]
        #n*n*log(n) + n + n + n
        sorted_strs = [ ''.join(sorted(str)) for str in strs]
        words_set = set(sorted_strs)
        words_map = { w: [] for w in words_set }

        for i in range(len(sorted_strs)):
            words_map.get(sorted_strs[i]).append(strs[i])


        return words_map.values()