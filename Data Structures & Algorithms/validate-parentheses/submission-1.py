class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']': '[', ')': '(', '}': '{'}
        stack = []

        for brck in s:
            if brck in brackets.values(): 
                stack.append(brck)
            else:
                if len(stack) > 0 and stack[-1] == brackets[brck]:
                    stack.pop(-1)
                else: 
                    return False
        return len(stack) == 0
