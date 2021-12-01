#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for x in words:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        res = sorted(d, key=lambda x: (-d[x], x))
        return res[:k]
# @lc code=end

