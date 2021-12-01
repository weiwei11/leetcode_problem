#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        flag = False
        for a in zip(*strs):
            # print(a)
            b = a[0]
            for x in a:
                if x != b:
                    flag = True
                    break
            if flag:
                break
            i += 1
        return strs[0][:i]
                    
# @lc code=end

