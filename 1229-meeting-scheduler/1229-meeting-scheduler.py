class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        
        
        slots1 = sorted(slots1, key=lambda x: x[0])
        slots2 = sorted(slots2, key=lambda x: x[0])
        
        first_p = 0
        
        second_p = 0
        
        
        while first_p < len(slots1) and second_p < len(slots2):
            
            
            r_int = min(slots1[first_p][1], slots2[second_p][1])
            l_int = max(slots1[first_p][0], slots2[second_p][0])
                
                
            if r_int - l_int >= duration:

                return [l_int, l_int + duration]

            if slots1[first_p][1] < slots2[second_p][1]:

                first_p += 1

            else:
                second_p += 1
            
        return []