# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isMirror(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True

        if tree1 is not None and tree2 is not None:
            if tree1.val == tree2.val:
                return (self.isMirror(tree1.left, tree2.right) and
                        self.isMirror(tree1.right, tree2.left))

        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)


test = Node(1)
test.left = Node(2)
test.right = Node(2)
test.left.left = Node(2)
test.right.left = Node(2)

s = Solution()
s.isSymmetric(test)