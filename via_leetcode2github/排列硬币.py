class Solution:
    def arrangeCoins(self, n: int) -> int:
        c = 0
        while n > c:
            c += 1
            n -= c
        return c
