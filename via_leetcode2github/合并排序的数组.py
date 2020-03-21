class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        #三指针逆序
        ans1, ans2 = m - 1, n - 1
        cur = m+n-1
        while ans1 >-1 and ans2 >-1:
            if A[ans1] < B[ans2]:
                A[cur] = B[ans2]
                ans2 -= 1
                cur -= 1
            else:
                A[cur] = A[ans1]
                ans1 -= 1
                cur -= 1
        if ans2 != -1:
            A[:ans2+1] = B[:ans2+1]
        return A



