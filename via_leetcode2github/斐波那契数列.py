class Solution:
    def fib(self, n: int) -> int:
        if n<= 1:
            return n
        A = [0,1]
        for _ in range(n-1):
            A.append(A[-1] + A[-2])
        return A[-1] % 1000000007

