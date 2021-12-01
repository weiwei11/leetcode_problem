#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = collections.Counter(magazine)
        for x in ransomNote:
            if counts[x] == 0:
                return False
            else:
                counts[x] -= 1
        return True

# @lc code=end

