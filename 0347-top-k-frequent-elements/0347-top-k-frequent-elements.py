class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
            
        print(countMap)
        
        uniqueNums = []
        for (uniqueNum, count) in countMap.items():
            uniqueNums.append((count, uniqueNum))
        
        
        uniqueNums = sorted(uniqueNums, reverse=True)
        ans = [ num for (count, num) in uniqueNums ]
        
        print(ans)
        return ans[:k]