from typing import List

# 1535. find the winner of an Array Game
class Solution1535:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        win_count = 0
        curr_max = arr[0]

        for i in range(1,n):
            if arr[i] < curr_max:
                win_count += 1
            else:
                if win_count >= k:
                    return curr_max
                curr_max = arr[i]
                win_count = 1

        return curr_max