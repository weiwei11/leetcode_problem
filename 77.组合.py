#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [[i] for i in range(1, n+1)]
        for _ in range(k-1):
            res = [[i]+c for c in res for i in range(1, c[0])]
        return res
        
        
# @lc code=end

