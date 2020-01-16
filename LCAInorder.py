# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.final = None
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

    def helper(self, root, ino, p, q):
        if root is None:
            return None

        if len(ino) < 0:
            return None

        indexOf = ino.index(root.val)
        leftIn = ino[:indexOf]
        rightIn = ino[indexOf+1:]

        if root.val == p and (q in leftIn or q in rightIn):
            self.final = root

        if root.val == q and (p in leftIn or p in rightIn):
            self.final = root

        if (p in leftIn and q in rightIn) or (q in leftIn and p in rightIn):
            self.final = root

        self.helper(root.left, leftIn, p , q)
        self.helper(root.right, rightIn, p , q)

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        inorder = self.inorderTraversal(root)
        self.helper(root, inorder, p.val, q.val)

        return self.final

s= Solution()
test = TreeNode(1)
test.left = TreeNode(2)
# test.right = TreeNode(1)
# test.left.left = TreeNode(6)
# test.left.right = TreeNode(2)
# test.left.right.left = TreeNode(7)
# test.left.right.right = TreeNode(4)
# test.right.left = TreeNode(0)
# test.right.right = TreeNode(8)
print(s.lowestCommonAncestor(test, test,test.left))




