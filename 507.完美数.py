#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        s = 1

        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                s = s + i + num // i
            if s > num:
                return False
        return s == num
# @lc code=end

