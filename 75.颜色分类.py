#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for x in nums:
            count[x] += 1
        begin = 0
        for i in range(count[0]):
            nums[begin] = 0
            begin += 1

        for i in range(count[1]):
            nums[begin] = 1
            begin += 1
        
        for i in range(count[2]):
            nums[begin] = 2
            begin += 1
        
        
# @lc code=end

