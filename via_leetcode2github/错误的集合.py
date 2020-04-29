class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nset = set(nums)
        double_number = sum(nums) - sum(nset)
        miss_number = int((1+n) * n / 2 - sum(nset))
        
        return [double_number, miss_number]      

