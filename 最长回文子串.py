class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = len(s)
        if m < 2:
            return s
        start_index = 0
        max_len = 1
        dp = [[False]*m for _ in range(m)]
        for j in range(1,m):
            for i in range(0,j):
                if s[i] == s[j]:
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    res_len = j-i+1
                    if res_len > max_len:
                        max_len = res_len
                        start_index = i
        return s[start_index: start_index + max_len]
