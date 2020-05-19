class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[::-1] == s:
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                a = s[l:r]
                b = s[l+1:r+1]
                if any((a == a[::-1], b == b[::-1])):
                    return True
                return False

