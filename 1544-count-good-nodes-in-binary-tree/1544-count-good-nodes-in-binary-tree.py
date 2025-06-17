# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1

        def dfs(node,highest,count):
            if node == None:
                return count
            if highest <= node.val:
                highest = node.val
                count+=1
            count = dfs(node.left,highest,count)
            count = dfs(node.right,highest,count)
            return count
        
        return dfs(root,root.val,0)

