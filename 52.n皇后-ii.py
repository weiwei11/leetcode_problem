#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1: return 1

        self.count = 0
        self.dfs([-1] * n, 0)
        return self.count

    def dfs(self, solve, i):
        if i == len(solve):
            self.count += 1
        
        for j in range(len(solve)):
            if self.valid(solve, i, j):
                solve[i] = j
                self.dfs(solve, i+1)
    
    def valid(self, solve, n, i):
        for j in range(n):
            if i == solve[j] or abs(i - solve[j]) == n - j:
                return False
        return True
         
# @lc code=end

