# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 1
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root and not(root.left) and not(root.right):
            return 0
        res = 0
        queue = [root]
        while any(queue):
            for i in range(0, len(queue), 2):
                if queue[i] and not(queue[i].left) and not(queue[i].right):
                    res += queue[i].val
            num = len(queue)
            while num:
                q = queue.pop(0)
                if q: queue += [q.left, q.right]
                num -= 1
        return res
