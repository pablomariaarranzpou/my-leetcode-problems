class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 0
        hashmap = {}
        
        for i in range(len(nums)):
            
            num = nums[i]
            
            if num not in hashmap:
                hashmap[num] = 1
                nums[k] = nums[i]
                k += 1
            elif hashmap[num] == 1:
                hashmap[num] += 1
                nums[k] = nums[i]
                k+= 1
            
        return k        

         
        