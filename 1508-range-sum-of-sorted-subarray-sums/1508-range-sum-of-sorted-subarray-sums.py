class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        sums = []
        for i in range(len(nums)):
            suma = 0
            for j in range(i, len(nums)):
                suma = suma + nums[j]
                sums.append(suma)
        
        return int(sum(sorted(sums)[left - 1: right])% 1000000007)
        