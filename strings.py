from collections import deque
from typing import List

# 344. Reverse String
class Solution344:
    # Build-in function
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

    def reverseString(self, s: List[str]) -> None:
        #recursion
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)    
    
    def reverseString2(self, s: List[str]) -> None:
        #two pointers
        left, right = 0, len(s) - 1
        while left < right:
            s[left],s[right] = s[right], s[left]
            left, right = left + 1, right - 1


# 541. Reverse String II
class Solution541:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])

        return "".join(a)
    
    def reverseStr1(self, s: str, k: int) -> str:
        i = 0
        res = ''
        while i < len(s):
            res += s[i:i+k][::-1]
            res += s[i+k: i + 2*k]
            i += 2 * k

        return res
    

# 151. Reverse Words in a String
class Solution151:
    # 1. buildin-in function
    # time: O(n), Space: O(n)
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
    
    # 2. Deque of words
    # time: O(n), Space: O(n)
    def reverseWords1(self, s: str) -> str:
        left, right = 0, len(s) - 1

        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1

        while left <= right and s[right] == ' ':
            right -= 1

        d, word = deque(), []

        #push word by word in front of deque
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.appendZ(s[left])
            left += 1

        d.appendleft(''.join(word))

        return " ".join(d)

    # 3. Methord 3
    # time: O(n), Space: O(n)
    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right],l[left]
            left, right = left + 1, right - 1

    def trim_spaces(self, s:str) -> list:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left < right and s[left] == ' ':
            left += 1

        # remove trailing spaces
        while left < right and s[right] == ' ':
            right -= 1

        # reduce multiple spaces to single one
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1

        return output
    
    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # go the end of the word
            while end < n and l[end] != ' ':
                end += 1
            
            #reverse the word
            self.reverse(l, start, end - 1)

            # move to the next word
            start = end + 1
            end += 1

    def reverseWords2(self, s: str) -> str:
        l = self.trim_spaces(s)

        # reverse the whole string
        self.reverse(l, 0, len(l) - 1)

        # reverse each word
        self.reverse_each_word(l)

        return ''.join(l)

# try new test
