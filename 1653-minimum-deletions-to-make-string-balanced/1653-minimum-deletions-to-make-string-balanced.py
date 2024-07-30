class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        n = len(s)
        a_c = sum(1 for ch in s if ch == "a")

        b_c = 0
        min_deletions = n

        for cha in s:
            if cha == "a":
                a_c -= 1
            min_deletions = min(min_deletions, a_c + b_c)
            if cha == "b":
                b_c += 1

        return min_deletions
                
            
        