#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
import random
class RandomizedSet:

    def __init__(self):
        self.d2i = {}
        self.i2d = []


    def insert(self, val: int) -> bool:
        # print(self.d2i)
        if val not in self.d2i:
            self.d2i[val] = len(self.i2d)
            self.i2d.append(val)
            return True
        return False


    def remove(self, val: int) -> bool:
        if val not in self.d2i:
            return False
        else:
            idx = self.d2i[val]
            self.i2d[idx] = self.i2d[-1]
            self.d2i[self.i2d[idx]] = idx
            self.d2i.pop(val)
            self.i2d.pop()
            return True


    def getRandom(self) -> int:
        return random.choice(self.i2d)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

