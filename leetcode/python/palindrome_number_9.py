class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        lenn = len(x)
        if lenn == 1:
            return True
        else:
            n = lenn // 2
        x1 = x[:n]
        x2 = x[-n:]
        return (x1 == x2[::-1])
            
        


x = 121
sol = Solution()
print (sol.isPalindrome(x))
