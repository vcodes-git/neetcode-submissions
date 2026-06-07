# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        q = deque([[float("-inf"), float("inf"), root]])

        while q:
            LBound, RBound, node = q.popleft()
            if not (LBound < node.val < RBound):
                return False
            else: 
                if node.left:
                    q.append([LBound, node.val, node.left])
                if node.right:
                    q.append([node.val, RBound, node.right])


        return True