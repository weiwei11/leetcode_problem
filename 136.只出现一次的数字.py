#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = nums[0]
        for x in nums[1:]:
            s ^= x
        return s
# @lc code=end

