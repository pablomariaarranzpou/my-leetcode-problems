class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = dict()
        sol = []
        
        for word in strs:
            selected = False
            sort = sorted(word)
            
            for key in groups.keys():
                if "".join(sort) == key:
                    groups[key].append(word)
                    selected = True
                    break
                    
            if(selected == False):           
                groups["".join(sort)] = [word]
                
        for gr in groups.values():
            sol.append(gr)
            
        return sol
            
            
        