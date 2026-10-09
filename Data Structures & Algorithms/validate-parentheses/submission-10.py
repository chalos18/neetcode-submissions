class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(","]":"[","}":"{"}
        stack = []

        for i in range(len(s)):
            if len(stack) != 0:
                top = stack[-1]
                if s[i] in pairs and pairs[s[i]] == top:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return len(stack) == 0
            