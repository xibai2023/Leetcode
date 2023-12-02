
from collections import defaultdict
import heapq
from typing import List

# 1814. Count Nice Pairs in an Array
class Solution1814:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            res = 0
            while num:
                res = res * 10 + num % 10
                num //= 10

        arr = []
        for i in range(len(nums)):
            arr.append(nums[i] - rev(nums[i]))

        dic = defaultdict(int) 
        ans = 0
        MOD = 10 ** 9 + 7
        for num in dic:
            ans = (ans + dic[num]) % MOD #hashmap中出现的次数就是相应的pair数
            dic[num] += 1

        return ans
      
#1838. Frequency of the Most Frequent Element
class Solution1838:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        res = 0
        curr = 0

        for right in range(len(nums)):
            target = nums[right]
            curr += target

            while(right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1

            res = max(res, right - left + 1)
        return res
    

# 1845. Seat Reservation Manager
class solution1845:
    class SeatManager:

        def __init__(self, n: int):
            # min heap to store all unreaserved seats.
            self.available_seats = [i for i in range(1, n+1)]

        def reserve(self) -> int:
            # Get the smallest-numbered unreserved seat from the min heap
            seat_number = heapq.heappop(self.available_seats)
            return seat_number

        def unreserve(self, seatNumber: int) -> None:
            # push the unreserved seat back into the min heap
            heapq.heappush(self.available_seats, seatNumber)


# 1877. Minimize Maximum Pair Sum in Array
class Solution1877:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        maxSum = 0
        left, right = 0, len(nums) - 1
        max_sum = float('-inf')

        while left < right:
            pair_sum = nums[left] + nums[right]
            max_sum = max(max_sum, pair_sum)
            left += 1
            right -= 1


        return max_sum

# 1887. Reduction Operations to Make the Array Elements Equal
class Solution1887:
    def reductionOperations(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        nums.sort()

        res = 0
        up = 0

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                up += 1

            res += up

        return res