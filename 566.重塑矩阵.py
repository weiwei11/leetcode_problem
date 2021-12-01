#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) == 0:
            return mat
        else:
            m = len(mat)
            n = len(mat[0])
            if m * n != r * c:
                return mat
            else:
                res = []
                for i in range(r):
                    s = []
                    for j in range(c):
                        idx = i * c + j
                        s.append(mat[idx//n][idx%n])
                    res.append(s)
                return res
# @lc code=end

