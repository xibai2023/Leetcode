class solution342:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        
        while n % 4 == 0:
            n /= 4
        
        return n == 1


a = solution342()
b = a.isPowerOfFour(16)

print(b)