# Given a binary search tree, write a function 
# kthSmallest to find the kth smallest element in
#  it.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        items = []
        if root is not None:
            #inorder traversal recursive
            self.inOrder(root, items.append)
        return items[k-1]
        
    def inOrder(self, root, visit):
        if root.left is not None:
            self.inOrder(root.left, visit)
        visit(root.val)
        if root.right is not None:
            self.inOrder(root.right, visit)