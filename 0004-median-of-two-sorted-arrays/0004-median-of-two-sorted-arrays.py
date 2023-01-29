class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total = nums1 + nums2
        total.sort()
        mid = len(total) // 2

        if len(total) % 2 != 0:
            return total[mid]
        
        return (total[mid - 1] + total[mid]) / 2
       