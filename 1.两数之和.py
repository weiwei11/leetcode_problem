#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d2i = dict([(x, i) for i, x in enumerate(nums)])
        for i, x in enumerate(nums):
            diff = target - x
            if diff in d2i.keys():
                i1, i2 = i, d2i[diff]
                if i1 != i2:
                    return [i1, i2]
        return []
            
# @lc code=end
