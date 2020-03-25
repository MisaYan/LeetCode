class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #二分法，时间复杂度O(log(n))。
        #求和法与异或法，时间复杂度O(n)。
        l, r = 0, len(nums)
        while l <r:
            mid = l + (r-l)//2
            if nums[mid] == mid:
                l= mid + 1
            else:
                r = mid
        return l
