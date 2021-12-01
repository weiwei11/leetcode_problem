#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            d[x] = d[x] + 1 if x in d else 1
        
        count = {}
        for z, v in d.items():
            if v in count:
                count[v].append(z)
            else:
                count[v] = [z]
        
        # print(count)
        res = []
        for c in range(len(nums), 0, -1):
            if not c in count:
                continue
            # print(count[c])
            if k >= len(count[c]):
                res.extend(count[c])
                k -= len(count[c])
            else:
                res.extend(count[c][:k])
            # print(res)
            # print(k)
            if k == 0:
                return res
            
        return res

            
# @lc code=end

