#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            a = int(str(x)[::-1])
            return a if a < (2 ** 31 - 1) else 0
        else:
            a = -int(str(-x)[::-1])
            return a if a > (-2 ** 31) else 0
# @lc code=end

