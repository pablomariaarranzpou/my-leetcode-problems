class Solution:
    def splitNum(self, num: int) -> int:
        
        nums = []
        
        for i in str(num):
            nums.append(int(i))
            
        nums.sort()
        
        num1 = ""
        num2 = ""
        
        for i in range(0, len(nums)):
            
            if i % 2:
                num1 += str(nums[i])
            else:
                num2 += str(nums[i])
        
        return int(num1) + int(num2)
