#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            d = [True, False, False, False, False, False, False, False, False, False]
            x = i
            f = True
            while x > 0:
                a = x % 10
                if a == 0 or (d[a] == False and i % a != 0):
                    f = False
                    break
                x //= 10
            if f:
                res.append(i)
        return res


# @lc code=end

