#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        else:
            a, b = 0, 1
            ac, bc = 0, 0
            for x in nums:
                if x == a:
                    ac += 1
                elif x == b:
                    bc += 1
                elif ac == 0:
                    a, ac = x, 1
                elif bc == 0:
                    b, bc = x, 1
                else:
                    ac -= 1
                    bc -= 1
            
            return [x for x in (a, b) if nums.count(x) > len(nums) // 3]
# @lc code=end

