#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        m = 1
        res = []
        for x in digits[::-1]:
            s = x + m
            m = s // 10
            n = s % 10
            res.append(n)
        if m > 0:
            res.append(m)
        return list(reversed(res))
        
        
# @lc code=end

