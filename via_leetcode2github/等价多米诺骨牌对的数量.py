class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        #collections.defaultdict用法:#1:将相同key值的value合到一个list中
                                     #2：为key计数
        
        ans = 0
        d = collections.defaultdict(int)
        for i, j in dominoes:
            num = i*10 + j if i<j else j*10 + i
            d[num] += 1
        for k in d.values():
            ans += int(k*(k-1)/2)
        return ans
