class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        front = 0
        rear = len(numbers) - 1
        
        
        while front < rear:
            
            r_v = numbers[rear]
                
            f_v = numbers[front]
            
            suma = f_v + r_v 
            
            if suma > target:
                rear -= 1
            elif suma < target:
                front += 1
                
            else:
                return [front + 1, rear + 1]
            
        return []
                
            
            
        