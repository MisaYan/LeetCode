class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k1 = collections.Counter(s)
        k2 = collections.Counter(t)
        if len(k1) >= len(k2):
            for k in k1:
                if k not in k2:
                    return False
                if k2[k] != k1[k]:
                    return False
        else:
            for k in k2:
                if k not in k1:
                    return False
                if k2[k] != k1[k]:
                    return False
        return True
