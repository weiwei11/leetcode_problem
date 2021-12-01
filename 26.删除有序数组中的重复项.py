#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        p = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[p-1]:
                pass
            else:
                nums[p] = nums[i]
                p += 1

        return p
            
# @lc code=end

