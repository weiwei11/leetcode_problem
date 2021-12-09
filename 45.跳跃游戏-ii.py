#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n, beg, end, count = len(nums), 0, 0, 0
        while end < n-1:
            count += 1
            m = end + 1
            for i in range(beg, end+1):
                if i + nums[i] >= n-1:
                    return count
                m = max(m, i + nums[i])
            beg, end = end+1, m
        return count
# @lc code=end

