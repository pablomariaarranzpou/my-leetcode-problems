class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_res = start ^ goal
        count = 0
        while xor_res:
            count += xor_res & 1
            xor_res >>= 1 
        return count
        