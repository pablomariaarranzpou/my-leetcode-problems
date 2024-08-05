class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        
        dicti = Counter(arr)
        k_th = 0
        
        for i in dicti:
            
            nums = dicti[i]
            if nums == 1:
                k_th += 1
                
                if(k_th == k):
                    return i
                
        return ""
                
                
                
        