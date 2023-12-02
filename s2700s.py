
# 2785. Sort Vowels in a String
class Solution2785:
    def sortVowels(self, s: str) -> str:
        #1. Collect Vowels and Sort
        vows = []

        for c in s:
            if c.lower() in "aeiou":
                vows.append(c)
        vows.sort()
        print(vows)
        #vows.reverse()

        reverseVows = sorted(vows,reverse=True)  # not modified "vows"
        print(reverseVows)
        print(vows)

        # Step 1: Collect vowels and sort them in descending order
        # vowels_sorted = sorted([c for c in s if c.lower() in 'aeiou'], reverse=True)

        # 2. Construct the Answer String
        res = []
        for c in s:
            if c.lower() in "aeiou":
                res.append(vows.pop())
            else:
                res.append(c)
        # 3. Join the characters to form the final string
        return "".join(res)
    

test = Solution2785()
newstr = test.sortVowels("lEetcOde")
print(newstr)

