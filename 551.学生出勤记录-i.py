#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        l_count = 0
        for x in s:
            if x == 'A':
                a_count += 1
                l_count = 0
            elif x == 'L':
                l_count += 1
            else:
                l_count = 0
            if a_count >= 2 or l_count >= 3:
                return False
        return True
# @lc code=end

