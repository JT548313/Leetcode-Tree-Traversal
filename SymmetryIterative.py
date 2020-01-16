# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False

        # Append root twice so that left and
        # right subtrees can be compared
        q = [root]
        q.append(root)

        while len(q)>0:
            left = q[0]
            q.pop()

            right = q[0]
            q.pop()

            if left.val != right.val:
                return False

            if left.left is None or right.right is None:
                return False

            elif left.left is not None and right.right is not None:
                q.append(left.left)
                q.append(right.right)

            if left.right is None or right.left is None:
                return False

            elif left.right is not None and right.left is not None:
                q.append(left.right)
                q.append(right.left)

        return True

