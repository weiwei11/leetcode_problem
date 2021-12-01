#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.index = 0

        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.index += 1
        return self.stack[self.index-1]

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[self.index]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.index >= len(self.stack)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

