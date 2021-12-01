#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = collections.Counter(s)
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1
# @lc code=end

