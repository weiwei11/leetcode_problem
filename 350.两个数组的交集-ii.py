#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = collections.Counter(nums1)
        res = []
        for x in nums2:
            if counts[x] > 0:
                res.append(x)
                counts[x] -= 1
                
        return res
# @lc code=end

