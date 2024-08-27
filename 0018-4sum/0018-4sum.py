class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)
        
        for i in range(len(nums) - 3):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i + 1, len(nums) - 2):
                
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                    
                k = j + 1
                h = len(nums) - 1
                while k < h:
                    suma = nums[i] + nums[j] + nums[k] + nums[h]

                    if suma < target:
                        k += 1
                        
                    elif suma > target:
                        h -= 1
                        
                    else:
                        
                        res.append([nums[i], nums[j], nums[k], nums[h]])
                        k += 1
                        h -= 1
                        while k<h and nums[k]==nums[k-1]:
                            k+=1
                        while k<h and nums[h]==nums[h+1]:
                            h-=1
                        
        return res
        