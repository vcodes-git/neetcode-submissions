class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        
        for token in tokens:
            if token in operators:
                b, a = int(stack.pop()), int(stack.pop())
                if token == "+":
                    res = a + b 
                elif token == '-':
                    res = a - b
                elif token == "*":
                    res = a * b
                else:
                    res = a / b
                stack.append(int(res))
            else:
                stack.append(token)
        
        return stack[0]

                

        