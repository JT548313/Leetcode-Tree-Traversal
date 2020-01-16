# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        postorder = []
        output = []
        final = []
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return

        postorder.append(root)

        while postorder:
            node = postorder.pop()
            output.append(node.val)

            if node.left:
                postorder.append(node.left)
            if node.right:
                postorder.append(node.right)

        while output:
            final.append(output.pop())

        return final


# Driver program to test above function
root = Node(1)
root.right = Node(2)
#root.left.left = Node(3)
#root.left.right = Node(5)
root.right.left = Node(3)

s = Solution()
s.postorderTraversal(root)