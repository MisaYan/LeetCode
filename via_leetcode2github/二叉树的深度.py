# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #递归
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    #BFS
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        treeHeight = 0
        queue = [root]      ###通过[]将某一层的树取出
        while queue:
            next_queue = []
            treeHeight += 1
            for node in queue:
                if not node:
                    continue
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return treeHeight



