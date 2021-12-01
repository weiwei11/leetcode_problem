#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        volume = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        while l < r:
            max_l, max_r = max(max_l, height[l]), max(max_r, height[r])
            if max_l <= max_r:
                volume += (max_l - height[l])
                l += 1
            else:
                volume += (max_r - height[r])
                r -= 1
        return volume
        
# @lc code=end

