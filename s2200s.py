# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution2265:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def postOrder(node):
            nonlocal res

            if not node:
                return 0, 0

            left_sum, left_count = postOrder(node.left)
            right_sum, right_count = postOrder(node.right)

            curr_sum = node.val + left_sum + right_sum
            curr_count = 1 + left_count + right_count

            if curr_sum //curr_count == node.val:
                res += 1

            return curr_sum, curr_count

        postOrder(root)
        return res