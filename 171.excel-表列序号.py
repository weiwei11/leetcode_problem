#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        d = {c: ord(c) - ord('A') + 1 for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        num = 0
        for x in columnTitle:
            num = num * 26 + d[x]
        return num
        
# @lc code=end

