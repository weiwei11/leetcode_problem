#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        m = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                m = max(m, cur)
                cur = 1
            else:
                cur += 1
        return max(m, cur)
        
# @lc code=end

