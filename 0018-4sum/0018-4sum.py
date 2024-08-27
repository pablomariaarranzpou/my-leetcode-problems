class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)
        seen = set()
        
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                
                k = j + 1
                h = len(nums) - 1
                while k < h:
                    suma = nums[i] + nums[j] + nums[k] + nums[h]

                    if suma < target:
                        k += 1
                        
                    elif suma > target:
                        h -= 1
                        
                    else:
                        
                        if (nums[i], nums[j], nums[k], nums[h]) not in seen:
                            seen.add((nums[i], nums[j], nums[k], nums[h]))
                            res.append([nums[i], nums[j], nums[k], nums[h]])
                        k += 1
                        h -= 1
                        
        return res
        