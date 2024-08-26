class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket_sort = [[] for i in range(len(nums) + 1)]
        
        
        for i in Counter(nums).items():
            
            bucket_sort[i[1]].append(i[0]) 
        
        res = []

        for i in range(len(bucket_sort) - 1, -1, -1):
            
            if len(res) > k - 1:
                break
                
            if bucket_sort[i]:
                
                for num in bucket_sort[i]:
                    
                    res.append(num)
                    
                    if len(res) > k - 1:
                        break
                        
        return res
                    
                    
                    
                    
            
            
        
        
        
        