#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sn = len(s) + 1
        pn = len(p) + 1
        t = [[False for _ in range(pn)] for i in range(sn)]
        t[0][0] = True
        for j in range(1, pn):
            if p[j-1] != '*':
                break
            t[0][j] = True
        
        for i in range(1, sn):
            for j in range(1, pn):
                if p[j-1] in {s[i-1], '?'}:
                    t[i][j] = t[i-1][j-1]
                elif p[j-1] == '*':
                    t[i][j] = t[i-1][j-1] or t[i][j-1] or t[i-1][j]
        return t[-1][-1]
        
# @lc code=end

