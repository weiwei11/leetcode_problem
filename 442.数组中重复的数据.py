#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            x = abs(x)
            if nums[x-1] < 0:
                res.append(x)
            else:
                nums[x-1] *= -1
        return res
# @lc code=end

