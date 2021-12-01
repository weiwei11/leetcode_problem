#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # if x < 4:
        #     return 1
        
        l = 0
        r = x
        while l <= r:
            m = (l + r) // 2
            if x == m * m:
                return m
            elif x < m * m:
                r = m - 1
            else:
                l = m + 1
        return r
# @lc code=end

