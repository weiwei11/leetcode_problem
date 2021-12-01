#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str2int(num):
            result  = 0
            for n in num:
                result = result * 10 + ord(n) - ord('0')
            return result
        return str(str2int(num1) + str2int(num2))
# @lc code=end

