#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        s = None
        for x in nums:
            if count == 0:
                s = x
            count = count + 1 if s == x else count - 1
        return s
# @lc code=end

