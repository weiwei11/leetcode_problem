#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1   
            else:
                l = mid + 1
        
        if target < nums[mid]:
            i = mid - 1
            while i >= 0 and target < nums[i]:
                i -= 1
            i += 1
        else:
            i = mid + 1
            while i < len(nums) and target > nums[i]:
                i += 1
            
        return i
# @lc code=end

