#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        pre, cur = 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                count += min(pre, cur)
                pre = cur
                cur = 1
        return count + min(pre, cur)

# @lc code=end

