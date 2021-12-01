#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            a = haystack.index(needle)
        except:
            a = -1
        return a
# @lc code=end

