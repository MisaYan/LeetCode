class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res= []
        tmp = 0
        for n in A:
            tmp = 2*tmp + n
            res.append(tmp%5==0)
        return res
                
