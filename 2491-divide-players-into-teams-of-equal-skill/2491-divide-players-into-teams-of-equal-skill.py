class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skills = sorted(skill)
        c = 0
        target = skills[0] + skills[-1]
        
        for i in range(len(skills) // 2):
            
            suma = skills[i] + skills[-i-1]
            
            if suma != target:
                return -1
            else:
                c += skills[i] * skills[-i-1]
            
        return c
        