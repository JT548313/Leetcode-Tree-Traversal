# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        stack = [root]
        while stack:
            nodes = []
            for index, item in enumerate(stack):
                if index+1 != len(stack):
                    item.next = stack[index + 1]
                if item.left:
                    nodes.append(item.left)
                if item.right:
                    nodes.append(item.right)
            if nodes:
                stack = nodes
                continue
            break

        return root
