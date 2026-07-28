class Solution:
    def isValid(self, s: str) -> bool:
        pairings = {'(':')', '{':'}', '[':']'}
        stack = []       
        if len(s) == 1:
            return False
        for char in s:
            if char in pairings.keys():
                stack.append(char)
            else:
                if char not in pairings.keys():
                    if len(stack) == 0 :
                        return False
                    top = stack[-1]
                    top_pairing = pairings[top]
                if char != top_pairing:
                    return False
                else:
                    stack.pop()
        return len(stack)== 0