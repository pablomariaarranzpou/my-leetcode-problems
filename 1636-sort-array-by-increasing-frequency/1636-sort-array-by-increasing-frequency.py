class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        freq = Counter(nums)
        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
        
        return sorted_nums
            
            
        