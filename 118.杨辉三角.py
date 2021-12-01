#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        else:
            for i in range(1, numRows):
                s = [1]
                for j in range(0, i - 1):
                    s.append(res[i-1][j] + res[i-1][j+1])
                s.append(1)
                res.append(s)
            return res
# @lc code=end

