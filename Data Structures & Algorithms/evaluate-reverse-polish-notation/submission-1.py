class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']

        for token in tokens:
            if token in operands:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == "+":
                    res = a + b
                elif token == "-":
                    res = a - b
                elif token == "*":
                    res = a * b
                elif token == "/":
                    res = a / b
                stack.append(res)
            else:
                stack.append(token)

        return int(stack.pop())