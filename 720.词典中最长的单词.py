#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        s = {""}
        res = ""
        for x in words:
            if x[:-1] in s:
                s.add(x)
                if len(x) > len(res):
                    res = x
        return res
        
# @lc code=end

