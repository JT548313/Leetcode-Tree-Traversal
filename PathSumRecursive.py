# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.res = False

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return None

        if sum - root.val == 0 and root.left is None and root.right is None:
            self.res = True

        self.hasPathSum(root.left, sum - root.val)
        self.hasPathSum(root.right, sum - root.val)

        return self.res


test = Node(1)
test.left = Node(2)
test.right = Node(3)
test.left.left = Node(4)
test.left.right = Node(5)
test.right.right = Node(6)

s = Solution()
print(s.hasPathSum(test, 10))

