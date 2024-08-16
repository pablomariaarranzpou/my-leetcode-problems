class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        max_value = float('-inf')
        max_value_index = -1
        second_max_value = float('-inf')
        
        min_value = float('inf')
        second_min_value = float('inf')
        min_value_index = -1
        
        for index, subarray in enumerate(arrays):
            
            cand_max = subarray[-1]
            cand_min = subarray[0]
            
            if cand_max > max_value:
                aux = max_value
                max_value = cand_max
                max_value_index = index
                second_max_value = aux
                
            elif cand_max > second_max_value:
                second_max_value = cand_max
                
            if cand_min < min_value:
                aux = min_value
                min_value = cand_min
                min_value_index = index
                second_min_value = aux
                
            elif cand_min < second_min_value:
                second_min_value = cand_min
                
        if max_value_index != min_value_index:
            return max_value - min_value
        else:
            return max(max_value - second_min_value, second_max_value - min_value)
                
                
            
                    