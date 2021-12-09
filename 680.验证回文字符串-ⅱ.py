#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def verify(s, l, r, n):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if n == 0:
                        return False
                    else:
                        return verify(s, l+1, r, n-1) or verify(s, l, r-1, n-1)
            return True
        
        return verify(s, 0, len(s)-1, 1)
            
        
# @lc code=end

