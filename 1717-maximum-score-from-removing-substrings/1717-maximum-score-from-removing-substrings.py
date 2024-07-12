class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def process_stack(s, first, second, points):
            stack = []
            gain = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    gain += points
                else:
                    stack.append(char)
            return ''.join(stack), gain

        total_gain = 0

        if x >= y:
            s, gain1 = process_stack(s, 'a', 'b', x)
            s, gain2 = process_stack(s, 'b', 'a', y)
        else:
            s, gain1 = process_stack(s, 'b', 'a', y)
            s, gain2 = process_stack(s, 'a', 'b', x)

        total_gain = gain1 + gain2
        return total_gain