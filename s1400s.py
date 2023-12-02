from typing import List

# 1441. Build an Array with stack operations
class Solution1441:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        current = 1

        for num in target:
            while current < num:
                res.append("Push")
                res.append("Pop")
                current += 1

            res.append("Push")
            current += 1

        return res
    

# a = Solution1441()
# target = [1,3]
# res = a.buildArray(target, 3)
# print(res)
