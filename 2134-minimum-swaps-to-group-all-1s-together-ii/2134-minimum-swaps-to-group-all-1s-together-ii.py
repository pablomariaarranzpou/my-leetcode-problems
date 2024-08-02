class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        new_arr = []
        ones = 0
        min_zeros = float('inf')
          
        n = len(nums)
        
        
        ones = nums.count(1)
        
        if ones == 0 or ones == n:
            return 0
        
        nums += nums
        

        current_zeros = sum(1 for i in range(ones) if nums[i] == 0)
        min_zeros = current_zeros

        for i in range(1, n):
            if nums[i - 1] == 0:
                current_zeros -= 1
            if nums[i + ones - 1] == 0:
                current_zeros += 1
            min_zeros = min(min_zeros, current_zeros)

        return min_zeros
                
            
            
        
        