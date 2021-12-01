#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        seta = set('qwertyuiop')
        setb = set('asdfghjkl')
        setc = set('zxcvbnm')
        # print(seta, setb, setc)
        res = []
        for x in words:
            setx = set(x.lower())
            if setx.issubset(seta) or setx.issubset(setb) or setx.issubset(setc):
                res.append(x)
        # res = [x for x in words if set(x).issubset(seta) \
            # or set(x).issubset(setb) or set(x).issubset(setc)]
        return res

# @lc code=end

