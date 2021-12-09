#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m = d = 0
        for i in range(len(nums)-k):
            d += nums[i+k] - nums[i]
            if d > m: m = d
        return (sum(nums[:k]) + m) / k
# @lc code=end

