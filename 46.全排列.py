#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, res, 0)
        return res

    def dfs(self, nums, res, d):
        if d == len(nums):
            res.append(nums.copy())
            
        for i in range(d, len(nums)):
            nums[i], nums[d] = nums[d], nums[i]
            self.dfs(nums, res, d+1)
            nums[i], nums[d] = nums[d], nums[i]
    
# @lc code=end

