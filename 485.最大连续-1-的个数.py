#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        count = 0
        for x in nums:
            if x == 1:
                count += 1
            else:
                m = max(m, count)
                count = 0
        return max(m, count)
            
        
# @lc code=end

