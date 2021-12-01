#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # if len(word) == 1: return True

        # mode = if word[0] 
        return word.isupper() or word.islower() or word.istitle()
# @lc code=end

