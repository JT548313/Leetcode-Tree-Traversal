# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return root

        res = [("0:"+root.val)]
        stack = [(root,0)]

        while stack:
            for cur, cur_idx in stack:
                next = []
                if cur.left:
                    next.append((cur.left, 2 * cur_idx + 1))
                    stack.append(2*cur_idx+1,cur.left)
                if cur.right:
                    next.append((cur.right, 2 * cur_idx + 2))
                    stack.append(2 * cur_idx + 2, cur.right)
            res = next
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return None

        def build_tree(node_dict, cur_idx):
            if cur_idx not in  node_dict:
                return None
            curr_node = Node(node_dict[cur_idx])
            curr_node.left = build_tree(node_dict, 2 * cur_idx + 1)
            curr_node.right = build_tree(node_dict, 2 * cur_idx + 2)
            return curr_node

        node_list = data.split(",")
        node_dict = {}
        for node in node_list:
            idx, val = node.split(":")
            node_dict[int(idx)] = int(val)
        root = build_tree(node_dict, 0)
        return root


# Your Codec object will be instantiated and called as such:
test = Node(3)
test.left = Node(2)
test.right = Node(4)
test.left.left = Node(3)

codec = Codec()
codec.deserialize(codec.serialize(test))