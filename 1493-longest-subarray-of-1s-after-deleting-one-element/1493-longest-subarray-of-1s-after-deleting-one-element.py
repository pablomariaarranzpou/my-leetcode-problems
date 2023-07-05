class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        zeros = 0
        longestWindow = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[start] == 0:
                    zeros -= 1
                start += 1
            
            longestWindow = max(longestWindow, i - start)
        
        return longestWindow
         
                
            
            
            