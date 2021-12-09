#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        if len(img) == 0: return img
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]

        def grid_avg(img, x, y, m, n):
            s = 0
            c = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if 0 <= x+i < m and 0 <= y+j < n:
                        s += img[x+i][y+j]
                        c += 1
            return s // c
        
        for i in range(m):
            for j in range(n):
                res[i][j] = grid_avg(img, i, j, m, n)
        return res
        
        
# @lc code=end

