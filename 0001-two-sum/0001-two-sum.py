class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_indices = [(num, i) for i, num in enumerate(nums)]
        
        nums_with_indices.sort()

        front = 0
        rear = len(nums) - 1

        while front < rear:
            current_sum = nums_with_indices[front][0] + nums_with_indices[rear][0]
            
            if current_sum == target:
                return [nums_with_indices[front][1], nums_with_indices[rear][1]]
            elif current_sum < target:
                front += 1
            else:
                rear -= 1

        return []
            
  