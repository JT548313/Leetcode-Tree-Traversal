# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return None

        root = preorder[0]
        rootNode = TreeNode(root)

        indexOf = inorder.index(root)
        indexOfPre = preorder.index(root)

        leftIn = inorder[:indexOf]
        rightIn = inorder[indexOf+1:]

        if len(leftIn)>0:
            rootNode.left = self.buildTree(preorder[indexOfPre+1:len(leftIn)+1],leftIn)
        if len(rightIn)>0:
            rootNode.right = self.buildTree(preorder[len(leftIn)+1:], rightIn)

        return rootNode

s = Solution()
preorder = [1,2,3]
inorder = [3,2,1]

print(s.buildTree(preorder, inorder))
