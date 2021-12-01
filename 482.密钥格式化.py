#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = []
        count = 0
        for x in s[::-1]:
            if x == '-':
                continue
            res.append(x.upper())
            count += 1
            if count == k:
                res.append('-')
                count = 0
        if res and res[-1] == '-':
            res.pop()
        return ''.join(reversed(res))
            

# @lc code=end

