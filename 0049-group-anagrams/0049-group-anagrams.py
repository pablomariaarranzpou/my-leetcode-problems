class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = dict()
        sol = []
        
        for word in strs:
            sort = "".join(sorted(word))
            
            if sort in groups.keys():
                groups[sort].append(word)
            else:           
                groups[sort] = [word]
                
        for gr in groups.values():
            sol.append(gr)
            
        return sol
            
            
        