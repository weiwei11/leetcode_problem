#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0, 0]
        for i in range(len(nums)):
            res.append(max(nums[i] + res[i], res[i+1]))
        # print(res)
        return res[-1]
        
# @lc code=end

