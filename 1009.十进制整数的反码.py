#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        l = 0
        s = n
        while n > 0:
            l += 1
            n //= 2
        return 2 ** (l) - 1 - s
#
# @lc code=end

