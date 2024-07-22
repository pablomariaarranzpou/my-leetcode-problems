class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dicta = {0:0,1:0,2:0}
        for i in nums:
            dicta[i] +=1

        index = 0
        for i, j in dicta.items():
            for _ in range(j):
                nums[index] = i
                index+=1
        return nums
        
            
            
        