class Solution:
    def search(self, nums: List[int], target: int) -> int:

        right = len(nums) - 1
        left = 0
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            # en caso de que este bien ordenado medio es mas grande que el de la izquierda
            if nums[mid] >= nums[left]:
                
                # comprobamos que el numero que buscamos esté en el intervalo de izquierda - mid (que esta bien ordenado)
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    
                # sino miramos el otro lado
                    left = mid + 1
            
            else:
                # en caso que este desordenado es decir el de el medio es mas pequeño que el de la izquierda
                
                # comprobamos si esta en el rango mid: right (que está bien ordenado)
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                # sino miramos el otro rango
                    right = mid - 1
                    
        return -1     