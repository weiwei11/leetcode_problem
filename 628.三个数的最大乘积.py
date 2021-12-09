#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        s = [float('inf')] * 2
        m = [float('-inf')] * 3
        for x in nums:
            if x <= s[0]:
                s[0] = x
                s.sort(reverse=True)
            if x >= m[0]:
                m[0] = x
                m.sort()
        # print(s, m)
        return max(s[0]*s[1]*m[2], m[0]*m[1]*m[2])
# @lc code=end

