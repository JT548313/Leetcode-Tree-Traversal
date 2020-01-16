# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return None

        root = postorder[-1]
        rootNode = TreeNode(root)

        indexOf = inorder.index(root)

        rootNode.left = self.buildTree(inorder[:indexOf], postorder[:indexOf])
        rootNode.right = self.buildTree(inorder[indexOf+1:], postorder[indexOf:-1])

        return rootNode

s = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(s.buildTree(inorder, postorder))
