#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s = s.lower()
        l, r = 0, len(s) - 1
        flag = True
        while l <= r:
            while l <= r and not s[l].isalnum():
                l += 1
            while l <= r and not s[r].isalnum():
                r -= 1
            if l <= r and s[l] != s[r]:
                flag = False
            l += 1
            r -= 1
        return flag
# @lc code=end

