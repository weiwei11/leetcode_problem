#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin = m = 0
        used = {}
        for i in range(len(s)):
            if s[i] in used and begin <= used[s[i]]:
                begin = used[s[i]] + 1
            else:
                m = max(m, i - begin + 1)
            used[s[i]] = i
        return m
# @lc code=end

