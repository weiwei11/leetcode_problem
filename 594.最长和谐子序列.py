#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
import collections
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        m = 0
        for x in set(nums):
            if x + 1 in counts:
                m = max(m, counts[x] + counts[x+1])
        return m

# @lc code=end

