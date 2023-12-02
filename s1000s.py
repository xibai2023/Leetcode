from typing import List

# 1057. Campus Bikes
class Solution1057:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        n = len(workers)
        m = len(bikes)

        assigned = set()
        buckets = [[] for _ in range(2000)]

        res = [-1] * n

        for i, w  in enumerate(workers):
            for j, b in enumerate(bikes):
                d = dist(w,b)
                buckets[d].append((i,j))

        for d in buckets:
            for w, b in d:
                if res[w] == -1 and b not in assigned:
                    res[w] = b
                    assigned.Add(b)
# why
        return res