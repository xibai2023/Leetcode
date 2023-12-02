from typing import List

# 1921. Eliminate Maximum Number of Monsters
class Solution1921:
    def eliminateMaximum(self, dist:List[int], speed: List[int]) -> int:
        t = []

        for d, s in zip(dist, speed):
            t.append(d/s, d, s)
        t.sort()

        killed = 0

        for x, (_,d, s) in enumerate(t):
            if s * x >= d:
                return killed
            
            killed += 1

        return killed
    
# 1930. Unique Length-3 Palindromic Subsequence
class Solution1930:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)

        res = 0

        for letter in letters:
            i,j = s.index(letter),s.rindex(letter)
            between = set()

            for k in range(i+1,j):
                between.add(s[k])

            res += len(between)

        return res
    
#1980. Find unique Binary String
class Solution1980:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def generate(curr):
            if len(curr) == n:
                if curr not in nums:
                    return curr
                return ""

            add_zero = generate(curr + "0")
            if add_zero:
                return add_zero

            return generate(curr + "1")

        n = len(nums)
        nums = set(nums)

        return generate("")