#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if len(mat) == 0: return []

        m, n = len(mat), len(mat[0])
        visited = set()
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        while q:
            x, y = q.popleft()
            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + d[0], y + d[1]
                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited:
                    mat[new_x][new_y] = mat[x][y] + 1
                    visited.add((new_x, new_y))
                    q.append((new_x, new_y))
        return mat


# @lc code=end

