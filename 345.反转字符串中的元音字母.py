#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        d = 'aeiouAEIOU'
        s = list(s)
        l, r = 0, len(s) - 1
        while l <= r:
            while l<=r and s[l] not in d:
                l += 1
            while l<=r and s[r] not in d:
                r -= 1
            if l<=r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        
        return ''.join(s)
# @lc code=end

