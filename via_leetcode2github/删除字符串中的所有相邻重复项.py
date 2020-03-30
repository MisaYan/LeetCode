class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for i in range(len(S)):
            stack.append(S[i])
            if len(stack)>=2 and stack[-1] == stack[-2]:
                stack.pop(-1)
                stack.pop(-1)
        return ''.join(stack)
            
            
