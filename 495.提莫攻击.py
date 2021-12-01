#
# @lc app=leetcode.cn id=495 lang=python3
#
# [495] 提莫攻击
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        beg = 0
        end = -1
        count = 0
        for x in timeSeries:
            count += (min(end, x-1) - beg + 1)
            beg = x
            end = beg + duration - 1
        return count + end - beg + 1
# @lc code=end

