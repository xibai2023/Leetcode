
from collections import defaultdict
from math import inf
from typing import Deque, List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        queue = Deque([root])

        while queue:
            curr_len = len(queue)
            curr_max = float("-inf")

            for _ in range(curr_len):
                node = queue.popleft()
                curr_max = max(curr_max, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(curr_max)

        return ans

# 501. Find Mode in Binary Search tree
class Solution501:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, counter):
            if not node:
                return

            counter[node.val] += 1
            dfs(node.left, counter)
            dfs(node.right, counter)

        counter = defaultdict(int)
        dfs(root, counter)

        max_freq = max(counter.values())

        res = []

        for key in counter:
            if counter[key] == max_freq:
                res.append(key)

        return res
# 509. Fibonacci number
class Solution509:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
            
        curr = 0
        prev1 = 1
        prev2 = 0
        
        for i in range(2, n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
            
        return curr
    
class Solution509_1:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        return self.fib(n-1) + self.fib(n-2)

# 573. Squirrel Simulation
class Solution573:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        res = 0
        maxDiff = -inf

        for y, x in nuts:
            dt = abs(y - tree[0]) + abs(x - tree[1])
            ds = abs(y - squirrel[0]) + abs(x - squirrel[1])

            maxDiff = max(maxDiff, dt - ds) 
            res += dt * 2

        return res - maxDiff