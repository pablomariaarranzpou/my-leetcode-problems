class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashmap = {}
        
        for i in range(len(nums)):
            
            new = nums[i]
            
            if new in hashmap and abs(hashmap[new] - i) <= k:
                return True
            else:
                hashmap[new] = i
            
        return False
                
                
        