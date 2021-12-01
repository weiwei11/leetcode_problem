#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'
        num = num if num >= 0 else 2 ** 32 + num
        d = {i: str(i) for i in range(10)}
        d.update({10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'})

        s = ''
        while num > 0:
            s = d[num % 16] + s
            num = num // 16
        return s
# @lc code=end

