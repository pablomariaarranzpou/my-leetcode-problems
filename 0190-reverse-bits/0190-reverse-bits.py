class Solution:
    def reverseBits(self, n: int) -> int:
        n='{:032b}'.format(n)
        n=n[::-1]
        return (int(n,2))
        
        