# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        preorder = []
        output = []
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return

        preorder.append(root)

        while len(preorder) > 0:
            node = preorder.pop()
            output.append(node.val)

            if node.right:
                preorder.append(node.right)
            if node.left:
                preorder.append(node.left)
        return output


# Driver program to test above function
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

s = Solution()
s.preorderTraversal(root)