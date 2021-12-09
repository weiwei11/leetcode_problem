#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = collections.Counter(s1)
        k = len(s1)
        for i in range(len(s2)-k+1):
            sub = s2[i:i+k]
            d2 = collections.Counter(sub)
            if d1 == d2:
                return True
        return False

        
# @lc code=end

