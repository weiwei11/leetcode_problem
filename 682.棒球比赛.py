#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for i in range(len(ops)):
            if ops[i] == '+':
                scores.append(scores[-1] + scores[-2])
            elif ops[i] == 'D':
                scores.append(scores[-1] * 2)
            elif ops[i] == 'C':
                scores.pop()
            else:
                scores.append(int(ops[i]))
        return sum(scores)
        
# @lc code=end

