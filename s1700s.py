
from collections import defaultdict
import modulefinder
from typing import List

#1727. Largest Submatrix with Rearrangements
class Solution1727:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        res = 0

        for row in range(m):
            for col in range(n):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]

                curr_row = sorted(matrix[row], reverse = True)
                for i in range(n):
                    res = max(res, curr_row[i] * (i + 1))

        return res

class Solution1727_1:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        prev_row = [0] * n
        res = 0

        for row in range(m):
            curr_row = matrix[row][:]
            for col in range(n):
                if curr_row[col] != 0:
                    curr_row[col] += prev_row[col]

            sorted_row = sorted(curr_row, reverse=True)
            for i in range(n):
                res = max(res, sorted_row[i] * (i+1))

            prev_row = curr_row

        return res
    
# 1743. Restore the Array from Adjacent Pairs
# DFS
class Solution1743:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if adjacentPairs is None:
            return None
        
        graph = defaultdict(list)

        for x,y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)

        root = None
        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break

        def dfs(node, prev, res):
            res.append(node)
            for neighbor in graph[node]:
                if neighbor != prev:
                    dfs(neighbor, node, res)

        res = []
        dfs(root, None, res)

        return res
    
# 1759. Count Number of Homogenous Substrings:
class Solution1759:
    def countHomogenous(self, s: str) -> int:
        res = 0
        currCount = 0
        Mod = 10 ** 9 + 7

        for i in range(len(s)):
            if i == 0 or s[i] == s[i-1]:
                currCount += 1
            else:
                curCount = 1

            res = (res + currCount) % Mod
        return res
    

