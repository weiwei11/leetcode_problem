#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = list(s)
        res = []
        def dfs(s, res, d):
            # print(d)
            if d == len(s):
                res.append(''.join(s))
                return 
            
            if s[d].isalpha():
                a = s[d]
                s[d] = a.lower()
                dfs(s, res, d+1)
                s[d] = a.upper()
                dfs(s, res, d+1)
                s[d] = a
            else:
                dfs(s, res, d+1)
        dfs(s, res, 0)
        return res
        
# @lc code=end

