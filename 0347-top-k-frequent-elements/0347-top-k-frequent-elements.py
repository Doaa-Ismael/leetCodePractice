class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        n = len(nums)
        freq = [[] for i in range(n+1)]
        
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1    
        
        for (num, count) in countMap.items():
            freq[count].append(num)
            
        ans, count = [], 0
        i = n
        
        while count < k:
            for num in freq[i]:
                if count == k:
                    break
                ans.append(num)
                count += 1
            i -= 1
            
        return ans
    
            