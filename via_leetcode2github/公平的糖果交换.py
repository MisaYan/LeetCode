class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        tmp = (sum(A)-sum(B))//2
        for i in set(A):
            if i-tmp in set(B):
                return [i,i-tmp]

