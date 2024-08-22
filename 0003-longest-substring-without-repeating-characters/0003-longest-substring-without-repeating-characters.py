class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        letters = set()
        max_l = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            while char in letters:
                letters.remove(s[left])
                left += 1
            letters.add(char)
            max_l = max(max_l, len(letters))

        return max_l

