# Construct Binary Search Tree from Preorder Traversal
# Return the root node of a binary search tree that matches
#  the given preorder traversal.
# (Recall that a binary search tree is a binary tree where 
# for every node, any descendant of node.left has a value < node.val,
#  and any descendant of node.right has a value > node.val.
#   Also recall that a preorder traversal displays the value of
#  the node first, then traverses node.left, then traverses node.right.)
# It's guaranteed that for the given test cases there is always 
# possible to find a binary search tree with the given requirements.
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        #construct inorder 
        inorder = sorted(preorder)
        return self.bstfromPreorderInorder(preorder,inorder)
        
    def bstfromPreorderInorder(self, preorder, inorder):
        prelen = len(preorder)
        inlen = len(inorder)
        if prelen == 0 or inlen == 0:
            return
        root = TreeNode(preorder[0])
        rootIndex = inorder.index(preorder[0])
        root.left = self.bstfromPreorderInorder(preorder[1:rootIndex+1], inorder[:rootIndex])
        root.right = self.bstfromPreorderInorder(preorder[rootIndex+1:], inorder[rootIndex+1:])
        return root