class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']': '[', ')': '(', '}': '{'}
        stack = []

        for brck in s:
            if brck in brackets:
                if not(stack and stack.pop() == brackets[brck]):
                    return False
            else:
                stack.append(brck)
        
        return len(stack) == 0
