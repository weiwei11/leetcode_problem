#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1比特与2比特字符
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ret = True
        for x in bits[-2::-1]:
            if x: ret = not ret
            else: break
        return ret
# @lc code=end

