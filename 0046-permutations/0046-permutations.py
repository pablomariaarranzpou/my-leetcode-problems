from itertools import permutations 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = permutations(nums) 
        
        lista = []
        for i in perm:
            
            lista.append(list(i))
            
        return lista
            
            
        