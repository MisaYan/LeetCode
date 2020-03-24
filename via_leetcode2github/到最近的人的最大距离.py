class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        new = ''.join([str(x) for x in seats]).split('1')
        max_0 = max(len(x) for x in new)
        return max((max_0+1)//2, len(new[0]), len(new[-1]))



