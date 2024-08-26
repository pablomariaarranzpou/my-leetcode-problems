class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
    
        res = []
        
        for i in sorted(Counter(nums).items(), key=lambda x: x[1], reverse = True)[:k]:
            
            res.append(i[0])
            
        return res
            
            
        
        
        
        