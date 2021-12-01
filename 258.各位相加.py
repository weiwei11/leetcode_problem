#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num 

        s = num % 9
        return s if s else 9
# @lc code=end

