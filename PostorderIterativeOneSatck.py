# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def peek(self, stack):
        if len(stack) > 0:
            return stack[-1]
        return None

    def postorderTraversal(self, root):
        postorder = []
        output = []

        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return

        while(True):
            while root:
                if root.right is not None:
                    postorder.append(root.right)
                postorder.append(root)
                root = root.left

            root = postorder.pop()

            if root.right is not None and self.peek(postorder) == root.right:
                postorder.pop()
                postorder.append(root)
                root = root.right

            else:
                output.append(root.val)
                root = None

            if (len(postorder) <= 0):
                break

        return output


# Driver program to test above function
test = Node(1)
test.left = Node(8)
test.right = Node(2)
test.left.left = Node(3)
test.left.right = Node(5)
test.right.left = Node(4)

s = Solution()
s.postorderTraversal(test)