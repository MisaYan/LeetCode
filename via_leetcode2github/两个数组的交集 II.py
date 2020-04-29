class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums1):
            if num in nums2:
                res.append(num)
                nums2.pop(nums2.index(num))
        return res
                
