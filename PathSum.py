# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return None

        s = [(root, sum)]

        while len(s) > 0:
            r = s.pop()

            if r[0] is None:
                continue

            res = r[1] - r[0].val

            if res == 0 and r[0].left is None and r[0].right is None:
                return True

            s.append([r[0].left, res])
            s.append([r[0].right, res])

        return False

test = Node(1)
test.left = Node(2)
test.right = Node(3)
test.left.left = Node(4)
test.left.right = Node(5)
test.right.right = Node(6)

s = Solution()
print(s.hasPathSum(test, 10))
