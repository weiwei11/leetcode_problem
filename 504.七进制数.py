#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return '0'

        f = '' if num >= 0 else '-'
        num = abs(num)
        res = []
        while num > 0:
            res.append(str(num % 7))
            num //= 7
        res.append(f)
        return ''.join(reversed(res))
            
# @lc code=end

