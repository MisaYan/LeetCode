class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for n in ops:
            if n == '+':
                stack.append(stack[-1]+ stack[-2])
            elif n == 'D':
                stack.append(2 * stack[-1])
            elif n == 'C':
                stack.pop(-1)
            else:
                stack.append(int(n))
            
        return sum(stack)
            
            
