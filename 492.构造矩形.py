#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

# @lc code=start
import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(math.sqrt(area))
        while w > 0:
            if area % w == 0:
                return [area // w, w]
            else:
                w -= 1
        return [area, 1]
# @lc code=end

