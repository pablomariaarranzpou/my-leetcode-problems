class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = dict()
        sol = []
        
        for word in strs:
            selected = False
            sort = "".join(sorted(word))
            
            for key in groups.keys():
                if sort == key:
                    groups[key].append(word)
                    selected = True
                    break
                    
            if not selected:           
                groups[sort] = [word]
                
        for gr in groups.values():
            sol.append(gr)
            
        return sol
            
            
        