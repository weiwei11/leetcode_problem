#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ''
        cur_count = 0

        for x in s:
            if x == '[':
                stack.append(cur_str)
                stack.append(cur_count)
                cur_str = ''
                cur_count = 0
            elif x == ']':
                num = stack.pop()
                pre_str = stack.pop()
                cur_str = pre_str + cur_str * num
            elif x.isdigit():
                cur_count = cur_count * 10 + int(x)
            elif x.isalpha():
                cur_str += x
        return cur_str
        
# @lc code=end

