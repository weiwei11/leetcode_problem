#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        count = [0]
        for i in range(1, n + 1):
            count.append(count[i // 2] + i % 2)
        return count
# @lc code=end

