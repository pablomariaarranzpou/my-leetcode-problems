class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i[0] for i in sorted(Counter(nums).items(), key=lambda x: x[1], reverse = True)[:k]]
            
            
        
        
        
        