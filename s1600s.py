from typing import List

# 1662. Check if two string arrays are equivalent
class Solution1662:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ''.join(word1)
        s2 = ''.join(word2)

        return s1 == s2

# 1685. Sum of Absolute Differences in a sorted array
class Solution1685:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) == 0:
            return []
        #prefix sum
        n = len(nums)
        total_sum = sum(nums)

        left_sum = 0
        res = []

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]

            left_count = i
            right_count = n - 1 - i

            left_total = left_count * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]

            res.append(left_total + right_total)
            left_sum += nums[i]

        return res