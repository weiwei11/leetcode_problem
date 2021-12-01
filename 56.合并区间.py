#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for x in intervals:
            if res and res[-1][1] >= x[0]:  # merge
                res[-1] = [res[-1][0], max(res[-1][1], x[1])]
            else:
                res.append(x)
        return res
            
        
# @lc code=end

