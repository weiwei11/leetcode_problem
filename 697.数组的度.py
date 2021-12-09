#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        d = {}
        m = 0
        min_len = 0
        for i in range(len(nums)):
            if nums[i] in d:
                x = d[nums[i]]
                d[nums[i]] = [x[0]+1, x[1], i]
            else:
                d[nums[i]] = [1, i, i]
            
            x = d[nums[i]]
            if x[0] > m:
                m = x[0]
                min_len = x[2] - x[1] + 1
            elif x[0] == m and x[2] - x[1] + 1 < min_len:
                m = x[0]
                min_len = x[2] - x[1] + 1
        return min_len
                
                
        
# @lc code=end

