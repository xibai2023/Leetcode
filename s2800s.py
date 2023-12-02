

# 2849. Determine if a cell is Reachable at a given time
class Solution2849:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        width = abs(sx - fx)
        height = abs(sy - fy)

        if width == 0 and height == 0 and t == 1:
            return False
        
        return t >= max(width, height)