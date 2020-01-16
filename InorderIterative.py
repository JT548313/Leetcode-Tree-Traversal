# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        inorder = []
        output = []
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return

        while root is not None:
            inorder.append(root)
            root = root.left
            while root is None and len(inorder) > 0:
                node = inorder.pop()
                output.append(node.val)
                root = node.right
        return output


# Driver program to test above function
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(1)

s = Solution()
s.inorderTraversal(root)
