# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            min_larger_node = self.get_min(root.right)
            root.val = min_larger_node.val
            root.right = self.deleteNode(root.right, min_larger_node.val)
        return root

    def get_min(self, node: TreeNode) -> TreeNode:
        while node.left is not None:
            node = node.left
        return node
