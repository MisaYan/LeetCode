class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        new_arr = set(arr)
        res = []
        for n in new_arr:
            res.append(arr.count(n))
        return len(res) == len(set(res))
