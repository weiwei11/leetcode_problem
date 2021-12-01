#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split()
        s = pattern
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

# @lc code=end

