import collections
from typing import List


# 1. Two sum

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return [i, hashmap[complement]]
            
            hashmap[nums[i]] = i


# 5. Longest Palindromic Substring
class Solution5:
    # broute force: time - O(n^3)
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(i,j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        for length in range(len(s), 0 , -1):
            for start in range(len(s) - length + 1):
                if isPalindrome(start, start + length):
                    return s[start: start + length]

        return ""
""" C# code: same function like the above
    public string LongestPalindrome(string s) {
        if (string.IsNullOrEmpty(s))
            return s;

        for (int len = s.Length; len > 0; len--) {
            for (int start = 0; start <= s.Length - len; start++) {
                if (IsPalindrome(start, start + len - 1, s))
                    return s.Substring(start, len);
            }
        }
        return "";
    }

    private bool IsPalindrome(int i, int j, string s) {
        int left = i, right = j;

        while (left < right) {
            if (s[left] != s[right])
                return false;
            left++;
            right--;
        }
        return true;
    }

"""
  
# DP: time - O(n^2)
class solutio5_1:
    def longestPalindromeDP(self, s: str) -> str:
        if s == s[::-1]:
            return s
            
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = [0,0]
        start, end = 0, 0

        for j in range(n):
            for i in range(j+1):
                if i == j:
                    dp[i][j] = True
                    continue

                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i+1][j-1])
                #//j - i < 3 两个连续的字符如 "aa"

                if dp[i][j] and j - i > end -start:
                    start,end = i,j
   
        return s[start: end+1]
    """
    public string LongestPalindrome0(string s)
    {
        string res = "";
        if (s.Length == 0)
            return res;

        int n = s.Length, start = 0, end = 0;
        bool[,] dp = new bool[n, n];
        //from top to bottom, from left to right
        for (int j = 0; j < n; j++)
        {
            for (int i = 0; i <= j; i++)
            {
                if (i == j)
                {
                    dp[i, j] = true;
                    continue;
                }
                dp[i, j] = (s[i] == s[j] && (j - i < 3 || dp[i + 1, j - 1]));  
                //j - i < 3 两个连续的字符如 "aa"

                if (dp[i, j] && (j - i > end - start)) {
                    start = i;
                    end = j;
                }         
            }
        }
        return s.Substring(start, end - start + 1);
    }
    """

# 49. Group Anagrams
class Solution49:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
    
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        return list(anagrams.values())
