#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = 0
        while i < len(letters) and target >= letters[i]:
            i += 1
        return letters[i] if i < len(letters) else letters[0]
# @lc code=end

