class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = cur = 0
        n = len(s)
        for i in range(n):
            cur += s[i] in 'aeiou'
            if i >= k:
                cur -= s[i-k] in 'aeiou'
            res = max(res, cur)
        return res
