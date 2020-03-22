class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res =-float('inf')
        tmp = -float('inf')
        for n in nums:
            tmp = max(n, tmp+n)
            res = max(res, tmp)
        return res
            


