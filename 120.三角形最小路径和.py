#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = []
        m, n = len(triangle), 1
        for i in range(m):
            s = []
            for j in range(n):
                a = None
                if 0 <= i-1 < m and 0 <= j-1 < n-1:
                    a = res[i-1][j-1]
                if 0 <= i-1 < m and 0 <= j < n-1:
                    b = res[i-1][j]
                    a = min(a, b) if a else b
                a = triangle[i][j] + (a if a else 0)
                s.append(a)
            res.append(s)
            n += 1
        return min(res[-1])
                
                
                    

        
# @lc code=end

