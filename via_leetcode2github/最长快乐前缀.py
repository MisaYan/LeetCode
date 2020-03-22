class Solution:
    def longestPrefix(self, s: str) -> str:
        index = []
        for i in range(len(s)-1):
            if s[i] == s[-1]:
                index.append(i)
        for i in range(len(index)-1, -1, -1):
            if s[:index[i]] == s[len(s)-index[i]-1: -1]:
                return s[:index[i]+1]
        return ''


