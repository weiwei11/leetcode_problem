#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res, i = 0, 0
        for x in s:
            if i == len(g):
                break
            if g[i] <= x:
                res += 1
                i += 1
        return res
        
# @lc code=end

