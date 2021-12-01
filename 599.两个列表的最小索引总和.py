#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = dict([(v, i) for i, v in enumerate(list1)])
        d2i = {r: d[r] + i for i, r in enumerate(list2) if r in d}

        MIN = float('inf')
        res = []
        for k, v in d2i.items():
            if v < MIN:
                res = [k]
                MIN = v
            elif v == MIN:
                res.append(k)
        return res
# @lc code=end

