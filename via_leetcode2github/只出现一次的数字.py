class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """异或法
        1、交换律：a ^ b ^ c <=> a ^ c ^ b
        2、任何数于0异或为任何数 0 ^ n => n
        3、相同的数异或为0: n ^ n => 0"""
        
        a = 0
        for num in nums:
            a ^= num
        return a
