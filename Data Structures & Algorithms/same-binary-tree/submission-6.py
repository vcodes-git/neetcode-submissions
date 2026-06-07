# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p is None and q is None: 
        #     return True
        # elif p is None: return False
        # elif q is None: return False
        # elif p.val != q.val: return False
        
        # else: 
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 


        # BFS:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                node1 = q1.popleft()
                node2 = q2.popleft()

                if node1 is None and node2 is None:
                    continue
                if node1 is None or node2 is None or node1.val!=node2.val:
                    return False
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right) 
        return True

        