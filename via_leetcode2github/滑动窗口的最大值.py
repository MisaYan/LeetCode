class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = []
        res = []
        if not nums:
            return []
        for i in range(k):
            stack.append(nums[i])
        Max = max(stack)
        res.append(Max)
        for j in range(k, len(nums)):
            stack.append(nums[j])
            stack.pop(0)
            res.append(max(stack))
        return res
        

