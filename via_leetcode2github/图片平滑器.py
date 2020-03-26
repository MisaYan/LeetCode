class Solution(object):
    def imageSmoother(self, M):
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in range(R)]

        for i in range(R):
            for j in range(C):
                count = 0
                for nr in (i-1, i, i+1):
                    for nc in (j-1, j, j+1):
                        if 0<= nr <R and 0<= nc <C:
                            ans[i][j] += M[nr][nc]
                            count += 1
                ans[i][j] //= count
        return ans
                

