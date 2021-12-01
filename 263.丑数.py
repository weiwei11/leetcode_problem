#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1: return True
        else:
            while n > 0 and n % 2 == 0:
                n = n // 2
            while n > 0 and n % 3 == 0:
                n = n // 3
            while n > 0 and n % 5 == 0:
                n = n // 5
            # print(n)
            return n == 1
# @lc code=end

