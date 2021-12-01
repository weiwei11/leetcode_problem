#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            s = guess(m)
            if s == 0:
                return m
            elif s == -1:
                r = m - 1
            else:
                l = m + 1
        return 1

        
# @lc code=end

