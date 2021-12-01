#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return [str(h)+':'+'0'*(m<10)+str(m) for h in range(12) for m in range(60) if (bin(m)+bin(h)).count('1') == turnedOn]
# @lc code=end

