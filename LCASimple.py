# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Base Case
        if root is None:
            return None

        # If either n1 or n2 matches with root's key, report
        #  the presence by returning root (Note that if a key is
        #  ancestor of other, then the ancestor key becomes LCA
        if root.key == p or root.key == q:
            return root

            # Look for keys in left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # If both of the above calls return Non-NULL, then one key
        # is present in once subtree and other is present in other,
        # So this node is the LCA
        if left_lca and right_lca:
            return root

            # Otherwise check if left subtree or right subtree is LCA
        return left_lca if left_lca is not None else right_lca

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




