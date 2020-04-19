class Solution:
    def reformat(self, s: str) -> str:
        l1 = []
        l2 = []
        for i in s:
            if i.isdigit():
                l1.append(i)
            else:
                l2.append(i)
        res = ''
        if len(l1)- len(l2) == 1:
            for i in range(len(l1)-1):
                res += l1[i] + l2[i]
            res += l1[-1]

        elif len(l1) == len(l2):
            for i in range(len(l1)):
                res += l1[i] + l2[i]

        elif len(l2) - len(l1) == 1:
            for i in range(len(l2)-1):
                res += l2[i] + l1[i]
            res += l2[-1]
        return res
