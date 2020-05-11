class Solution:
    def twoSum(self, n: int) -> List[float]:
        ###记忆化递归（DP）
        dp = [[0] * (6*n+1) for _ in range(n+1)]
        for i in range(1,7): dp[1][i] = 1
        for i in range(2,n+1):
            for j in range(i, 6*i+1):
                for k in range(1,7):
                    if j-k < i-1:
                        break
                    dp[i][j] += dp[i-1][j-k]
        return [x/(6**n) for x in dp[n][n:6*n+1]]

