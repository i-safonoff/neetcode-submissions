class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = '+-*/'
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if token == '+':
                    stack.append(op1 + op2)
                if token == '-':
                    stack.append(op1 - op2)
                if token == '*':
                    stack.append(op1 * op2)
                if token == '/':
                    stack.append(int(op1 / op2))
        
        return stack.pop()