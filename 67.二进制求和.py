#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        res = []
        m = 0
        d = {'1': 1, '0': 0, 0: '0', 1: '1'}
        for i in range(min(len(a), len(b))):
            x = d[a[i]]
            y = d[b[i]]
            s = x + y + m
            res.append(d[s % 2])
            m = s // 2
        c = a if len(a) > len(b) else b
        begin = len(a) if len(a) < len(b) else len(b)
        for n in c[begin:]:
            x = d[n]
            s = x + m
            res.append(d[s % 2])
            m = s // 2
        if m > 0:
            res.append(d[m])
        return ''.join(reversed(res))

# @lc code=end

