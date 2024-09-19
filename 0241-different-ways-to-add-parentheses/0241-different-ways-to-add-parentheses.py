class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        n = len(expression)
        if n == 0:
            return []
        
        res = []
        
        
        if n == 1:
            return [int(expression)]
        
        if n == 2 and expression[0].isdigit():
            return [int(expression)]

        for i, current_char in enumerate(expression):

            if current_char.isdigit():
                continue

            left_results = self.diffWaysToCompute(expression[:i])
            right_results = self.diffWaysToCompute(expression[i + 1 :])


            for left_value in left_results:
                for right_value in right_results:

                    if current_char == "+":
                        res.append(left_value + right_value)
                    elif current_char == "-":
                        res.append(left_value - right_value)
                    elif current_char == "*":
                        res.append(left_value * right_value)

        return res
        
        
        
        
        
        
        