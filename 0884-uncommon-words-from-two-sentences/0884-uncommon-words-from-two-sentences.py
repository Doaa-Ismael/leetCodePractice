class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        wordsDict = dict()
        ans = []
        for w in s1.split(' '):
            wordsDict[w] = wordsDict.get(w, 0) + 1
                
        for w in s2.split(' '):
            wordsDict[w] = wordsDict.get(w, 0) + 1
        
        for w in wordsDict:
            if wordsDict.get(w) == 1:
                ans.append(w)
        
        return ans