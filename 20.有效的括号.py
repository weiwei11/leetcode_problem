#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')': '(', '}': '{', ']': '['}
        left = set(['(', '[', '{'])
        res = []
        flag = True
        for x in s:
            if x in left:
                res.append(x)
            else:
                r = pair[x]
                if len(res) == 0 or res.pop() != r:
                    flag = False
                    break
        if len(res) > 0:
            flag = False
        return flag
# @lc code=end

