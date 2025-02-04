from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque()
        nodes = []
        
        if root :
            queue.append(root)
            
        level = 0
        
        while queue :
            level_nodes = []
            for i in range(len(queue)) :
                cur = queue.popleft()
                level_nodes.append(cur.val)
                if cur.left :
                    queue.append(cur.left)
                if cur.right :
                    queue.append(cur.right)
            nodes.append(level_nodes)


                
        return nodes