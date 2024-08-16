class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        max_value = float('-inf')
        max_value_index = -1
        second_max_value = float('-inf')
        
        min_value = float('inf')
        second_min_value = float('inf')
        min_value_index = -1
        
        for index, subarray in enumerate(arrays):
            
            if subarray[-1] > max_value:
                aux = max_value
                max_value = subarray[-1]
                max_value_index = index
                second_max_value = aux
                
            elif subarray[-1] > second_max_value:
                second_max_value = subarray[-1]
                
            if subarray[0] < min_value:
                aux = min_value
                min_value = subarray[0]
                min_value_index = index
                second_min_value = aux
                
            elif subarray[0] < second_min_value:
                second_min_value = subarray[0]
                
                
        if max_value_index != min_value_index:
            return max_value - min_value
        else:
            return max(max_value - second_min_value, second_max_value - min_value)
                
                
            
                    