#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        return l
        
# @lc code=end

