class Solution:
    def isHappy(self, n: int) -> bool:
        #创建一个Hashset 记录循环数字，若重复出现则停止迭代
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            return total_sum
        
        seen = set()
        while n!= 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1
