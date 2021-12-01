#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        flag = [True]
        for i in range(1, len(s) + 1):
            flag.append(any([flag[j] and s[j:i] in wordDict for j in range(i)]))
        
        return flag[-1]
        
# @lc code=end

