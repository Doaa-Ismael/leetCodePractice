class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        for i in range(len(nums1)):
            index, num, ans = nums2.index(nums1[i]) + 1, nums1[i], -1
            nums1[i] = -1
            while index < len(nums2):
                if nums2[index] > num:
                    nums1[i] = nums2[index]
                    break;
                index += 1
            
        return nums1