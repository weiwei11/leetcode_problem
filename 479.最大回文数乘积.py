#
# @lc app=leetcode.cn id=479 lang=python3
#
# [479] 最大回文数乘积
#

# @lc code=start
import math
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        else:
            a = 0
            ma = 2 * 10 ** n
            while a < ma:
                upper = 10 ** n - a
                lower = int(str(upper)[::-1])
                p = a ** 2 - 4 * lower
                if p > 0 and int(math.sqrt(p)) ** 2 == p:
                    return (upper * 10 ** n + lower) % 1337
                a += 1
            
# @lc code=end

