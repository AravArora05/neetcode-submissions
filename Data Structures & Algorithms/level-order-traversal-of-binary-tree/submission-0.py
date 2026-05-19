# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        arr = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            arr1 = []
            for i in range(len(queue)):
                curr = queue.popleft()
                arr1.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            #so get each one from each level
            arr.append(arr1)
        return arr
                
                
        