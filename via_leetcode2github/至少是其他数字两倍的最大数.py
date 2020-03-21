class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = nums.index(max(nums))
        return res if sorted(nums)[-2] * 2 <= max(nums) else -1
