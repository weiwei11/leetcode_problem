#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        res = []
        start = end = nums[0] 
        for x in nums[1:]:
            if x == end + 1:
                end = x
            else:
                if start == end:
                    res.append(str(end))
                else:
                    res.append('{}->{}'.format(start, end))
                start = end = x
        if start == end:
            res.append(str(end))
        else:
            res.append('{}->{}'.format(start, end))
        return res
            
# @lc code=end

