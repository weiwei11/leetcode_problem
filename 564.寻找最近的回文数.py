#
# @lc app=leetcode.cn id=564 lang=python3
#
# [564] 寻找最近的回文数
#

# @lc code=start
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length, int_n = len(n), int(n)
        if int_n < 10 or int_n == 10 ** (length - 1): return str(int_n - 1)
        if int_n - 1 == 10 ** (length - 1): return str(int_n - 2)
        if int_n + 1 == 10 ** (length - 1): return str(int_n + 2)
        half = int(n[:(length+1)//2])
        tmp = [s[:length//2] + s[::-1] for s in [str(half + dx) for dx in (-1, 0, 1)]]
        return min(tmp, key=lambda x: (x==n, abs(int(x)-int_n)))

# @lc code=end