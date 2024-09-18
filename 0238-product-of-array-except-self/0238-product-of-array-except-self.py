class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)

        ans = [0] * length

        ans[0] = 1
        for i in range(1, length):
            ans[i] = nums[i - 1] * ans[i - 1]


        R = 1
        for i in reversed(range(length)):
            ans[i] = ans[i] * R
            R *= nums[i]
            
            
        return ans

            