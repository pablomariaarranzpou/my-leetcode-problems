class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        c=0
        for i in zip(*strs):
            if list(i)!=sorted(i):
                c+=1
        return c