#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def ser(root, res):
            if root:
                res.append(str(root.val))
                ser(root.left, res)
                ser(root.right, res)
            else:
                res.append('#')
        res = []
        ser(root, res)
        return ','.join(res) 
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deser(it):
            val = next(it)
            if val == '#':
                return None
            else:
                root = TreeNode(val)
                root.left = deser(it)
                root.right = deser(it)
                return root
        it = iter(data.split(','))
        root = deser(it)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

