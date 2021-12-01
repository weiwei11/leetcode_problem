#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[p] = nums[i]
                p += 1
        while p < len(nums):
            nums[p] = 0
            p += 1
        
        
# @lc code=end

