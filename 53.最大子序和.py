#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        c = nums[0]
        for x in nums[1:]:
            c = max(x, c + x)
            m = max(m, c)
        return m
        
# @lc code=end

