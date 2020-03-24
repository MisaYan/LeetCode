class Solution:
    #DP的两种写法
    '''def massage(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i-1], nums[i])
            else:
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]
    '''
    def massage(self, nums: List[int]) -> int:
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last+num, now)
        return now
