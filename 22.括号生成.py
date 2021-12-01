#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, parents):
            if not right: parents.append(p)
            if right > left: generate(p + ')', left, right-1, parents)
            if left: generate(p + '(', left-1, right, parents)
            return parents

        return generate('', n, n, [])
# @lc code=end

