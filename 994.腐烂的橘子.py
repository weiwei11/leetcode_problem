#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0: return 0

        q = deque()
        visited = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited.add((i, j))
                elif grid[i][j] == 2:
                    q.append((i, j))
        max_time = 0
        while visited and q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for c in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    if c in visited:
                        visited.remove(c)
                        q.append(c)
            max_time += 1
        return -1 if visited else max_time

# @lc code=end

