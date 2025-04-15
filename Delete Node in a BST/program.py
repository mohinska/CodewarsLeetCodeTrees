# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node_to_del, parent = self.find_key_node(root, key)
        if node_to_del in [None, []]:
            return root
        print(node_to_del)
        print(parent.val)

        side = 0 if parent.left == node_to_del else 1
        if node_to_del.left.val is None and node_to_del.right.val is None:
            if side == 0:
                parent.left = None
            else:
                parent.right = None
        elif node_to_del.left.val is not None:
            if side == 0:
                node_to_del.left.right = node_to_del.right
                parent.left = node_to_del.left
            else:
                node_to_del.left.right = node_to_del.right
                parent.right = node_to_del.left
        elif node_to_del.right.val is not None:
            if side == 0:
                node_to_del.right.left = node_to_del.left
                parent.left = node_to_del.right
            else:
                node_to_del.right.left = node_to_del.left
                parent.right = node_to_del.right
        return root

    def find_key_node(self, root, key, parent=None):
        if root is None:
            return None, None
        if root.val == key:
            return root, parent
        return (self.find_key_node(root.left, key, root)
                or self.find_key_node(root.right, key, root))
