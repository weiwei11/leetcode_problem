#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = [1]
        if rowIndex == 0:
            return pre
        else:
            for i in range(1, rowIndex+1):
                s = [1]
                for j in range(0, i-1):
                    s.append(pre[j] + pre[j+1])
                s.append(1)
                pre = s
            return pre
# @lc code=end

