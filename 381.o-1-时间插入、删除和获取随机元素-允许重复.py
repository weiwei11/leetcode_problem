#
# @lc app=leetcode.cn id=381 lang=python3
#
# [381] O(1) 时间插入、删除和获取随机元素 - 允许重复
#

# @lc code=start
import random
class RandomizedCollection:

    def __init__(self):
        self.d2i = {}
        self.i2d = []


    def insert(self, val: int) -> bool:
        # print(self.d2i)
        flag = val not in self.d2i
        if flag:
            self.d2i[val] = {len(self.i2d)}
            self.i2d.append(val)
        else:
            self.d2i[val].add(len(self.i2d))
            self.i2d.append(val)
            
        return len(self.d2i[val]) == 1


    def remove(self, val: int) -> bool:
        if val not in self.d2i or len(self.d2i[val]) == 0:
            return False
        else:
            idx = self.d2i[val].pop()
            last = self.i2d[-1]

            self.i2d[idx] = self.i2d[-1]
            self.d2i[last].add(idx)
            self.d2i[last].remove(len(self.i2d) - 1)

            # self.d2i.pop(val)
            self.i2d.pop()
            return True


    def getRandom(self) -> int:
        return random.choice(self.i2d)




# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

