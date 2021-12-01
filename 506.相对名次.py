#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = {s:i for i, s in enumerate(sorted(score, reverse=True))}
        return [str(rank[x] + 1) if rank[x] > 2 else ['Gold', 'Silver', 'Bronze'][rank[x]] + ' Medal'
                for x in score]
# @lc code=end

