class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a = sum(nums[:0])
        b = sum(nums[1:])

        for i in range(0, len(nums)-1):
            if a == b:
                return i
            a += nums[i]
            b -= nums[i+1]
        if a== b:
            return len(nums) - 1
        return -1
