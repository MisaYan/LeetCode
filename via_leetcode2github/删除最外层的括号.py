class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = ''
        for n in S:
            if n == '(':
                stack.append(n)
                if len(stack) > 1:
                    res += '('
            else:
                stack.pop()
                if len(stack) != 0:
                    res += ')'
        return res

