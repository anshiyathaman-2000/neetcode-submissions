# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



#Anoher way to solve this:
#   if not root:
    #  return None
   # stack=[root]
   # while stack:
      #  node=stack.pop()
      #  root.left,root.right=root.right,root.left
      #  if node.left:
        #    stack.append(node.left)
      #  if node.right:
        #    stack.append(node.right)
   # return root

    

























  


