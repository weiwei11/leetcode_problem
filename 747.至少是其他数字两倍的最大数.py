#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        m, s = nums[0], -1
        m_idx = 0
        for i in range(1, len(nums)):
            if nums[i] > s:
                s = nums[i]
                if nums[i] > m:
                    m, s = s, m
                    m_idx = i
        if s == 0: return m_idx
        return m_idx if m / s >= 2 else -1

# @lc code=end

