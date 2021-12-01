#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        while n:
            if n & 1:
                num += 1
            n = n >> 1
        return num
        
# @lc code=end

