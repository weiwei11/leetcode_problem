#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        p = 0
        m, n = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0: p += 1
                    if i == m-1 or grid[i+1][j] == 0: p += 1
                    if j == 0 or grid[i][j-1] == 0: p += 1
                    if j == n-1 or grid[i][j+1] == 0: p += 1
        return p
        
# @lc code=end

