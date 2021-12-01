#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        res = 0
        m = prices[0]
        for x in prices[1:]:
            res = max(res, x - m)
            m = min(m, x)

        return res
# @lc code=end

