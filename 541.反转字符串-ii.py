#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        f = True
        res = []
        beg = end = 0
        while beg < len(s):
            end = beg + k if beg + k < len(s) else len(s)
            if f:
                res.append(s[beg:end][::-1])
            else:
                res.append(s[beg:end])
            f = not f
            beg = end
        return ''.join(res)
        
        
# @lc code=end

