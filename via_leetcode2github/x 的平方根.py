class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        xk = x
        while xk > x/xk:
            xk = (xk + x/xk)//2
        return int(xk)
