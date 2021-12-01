#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = collections.Counter(s)
        length = 0
        f = 0
        for x in counts:
            if counts[x] % 2 == 1:
                f = 1
            length += (counts[x] // 2)
        return length * 2 + f
            

# @lc code=end

