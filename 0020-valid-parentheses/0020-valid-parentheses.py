class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        parenthesis = {')':'(', ']':'[', '}':'{'}

        if len(s) == 1:
            return False

        for i in s:

            if i in parenthesis.keys() and len(stack) != 0:
                last = stack.pop()

                if(last != parenthesis[i]):
                    return False
            else:
                stack.append(i)

        if(len(stack) != 0):

            return False
        return True