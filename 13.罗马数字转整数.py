#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        table = {0: 0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        flag = True
        res = 0
        pre = None
        n = 0
        for x in s:
            pre = n
            n = x
            a = table[pre]
            if pre == 'I' and (n == 'V' or n == 'X'):
                res -= a
            elif pre == 'X' and (n == 'L' or n == 'C'):
                res -= a
            elif pre == 'C' and (n == 'D' or n == 'M'):
                res -= a
            else:
                res += a
        res += table[n]
        return res

# @lc code=end

