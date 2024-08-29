class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        letras_actuals = set()
        last = 0
        max_l = 0

        for i in range(len(s)):

            char = s[i]

            while char in letras_actuals:

                letras_actuals.remove(s[last])
                last += 1

            letras_actuals.add(char)

            max_l = max(max_l, i - last + 1)

        return max_l