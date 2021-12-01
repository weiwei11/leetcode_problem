#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        else:
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1':
                        count += 1
                        self.dfs(grid, i, j)   
                        # print(i, j)
            return count 
    
    def dfs(self, grid, i, j):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]) \
            and grid[i][j] == '1':
            grid[i][j] = '#'
            self.dfs(grid, i, j-1)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
    
# @lc code=end

