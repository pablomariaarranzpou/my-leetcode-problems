class Solution:
    def minSwaps(self, s: str) -> int:
        stack = deque()
        count = 0
        for char in s:
   
            if char == "[":
                stack.append(char)
            else:
      
                if stack:
                    stack.pop()

                else:
                    count += 1
        return (count + 1) // 2