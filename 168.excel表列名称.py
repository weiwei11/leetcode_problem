#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        table = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        s = []
        while columnNumber > 0:
            columnNumber, b = (columnNumber-1) // 26, (columnNumber-1) % 26
            s.append(table[b])
        return ''.join(s[::-1])

        
# @lc code=end

