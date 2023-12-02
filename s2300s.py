from typing import List

# 2391. Minimum Amount of Time to Collect Garbage
class Solution2391:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0

        n = len(garbage)

        m,p,g = False,False,False
        for i in range(n-1,-1,-1):
            if not g and "G" in garbage[i]:
                g=True
                ans+=sum(travel[:i])
            if not m and "M" in garbage[i]:
                m=True
                ans+=sum(travel[:i])
            if not p and "P" in garbage[i]:
                p=True
                ans+=sum(travel[:i])
            if all([m,p,g]):
                break

        return len("".join(garbage))+ans
    
class Solution2391_1:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        tG, tP, tM = 0, 0, 0
        time = 0

        for i in range(n-1, -1, -1):
            x = garbage[i]
            time += len(x) 

            if tG == 0 and x.find('G') != -1: tG = i
            if tP == 0 and x.find('P') != -1: tP = i
            if tM == 0 and x.find('M') != -1: tM = i

        time += sum(travel[:tG]) + sum(travel[:tP]) + sum(travel[:tM])
        return time