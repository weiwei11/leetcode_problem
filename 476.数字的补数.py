#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        # l = 0
        # s = num
        # while num > 0:
        #     l += 1
        #     num //= 2
        # return 2 ** (l) - 1 - s

        return 2 ** (num.bit_length()) - 1 - num
# @lc code=end

