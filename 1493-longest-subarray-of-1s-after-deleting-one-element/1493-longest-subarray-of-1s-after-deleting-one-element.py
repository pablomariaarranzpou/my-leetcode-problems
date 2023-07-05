class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0;
        zeros = 0;
        longestWindow = 0;
        
        for i in range(len(nums)):

            zeros += (nums[i] == 0);
                          
            while (zeros > 1):
                zeros -= (nums[start] == 0)
                start += 1
            
              
            longestWindow = max(longestWindow, i - start)
        

        return longestWindow;
         
                
            
            
            