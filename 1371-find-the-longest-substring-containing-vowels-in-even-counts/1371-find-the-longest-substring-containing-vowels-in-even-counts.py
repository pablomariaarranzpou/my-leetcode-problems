class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        XOR = 0
        characters = [0] * 26
        characters[ord("a") - ord("a")] = 1
        characters[ord("e") - ord("a")] = 2
        characters[ord("i") - ord("a")] = 4
        characters[ord("o") - ord("a")] = 8
        characters[ord("u") - ord("a")] = 16
        mp = [-1] * 32
        longestSubstring = 0
        for i in range(len(s)):
            XOR ^= characters[ord(s[i]) - ord("a")]
            if mp[XOR] == -1 and XOR != 0:
                mp[XOR] = i
            longestSubstring = max(longestSubstring, i - mp[XOR])
        return longestSubstring