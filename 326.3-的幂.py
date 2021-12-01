#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power_list = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
        return n in power_list
# @lc code=end

