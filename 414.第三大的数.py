#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            if x in s:
                continue
            else:
                s.add(x)
                if len(s) > 3:
                    s.remove(min(s))
        if len(s) == 3:
            return min(s)
        else:
            return max(s)
# @lc code=end

