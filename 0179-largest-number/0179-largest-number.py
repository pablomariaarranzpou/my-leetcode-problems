class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums_s = [str(i) for i in nums]
        
        
        
            
        
        nums_s = sorted(nums_s, key=lambda x: x * 10, reverse =True)
        
        if nums_s[0] == '0':
            return "0"
        
        final = ""
               
        for i in nums_s:
            final += str(i)
        
        return final
        