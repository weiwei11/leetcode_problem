#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log(n, 4).is_integer()
# @lc code=end

