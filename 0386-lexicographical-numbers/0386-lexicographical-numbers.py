class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return [int(i) for i in sorted([str(i + 1) for i in range(n)])]
    
    
        