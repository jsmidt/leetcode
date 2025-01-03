# 13. Roman to Integer
# Author - Joseph Smidt
#

class Solution:
    def romanToInt(self, s: str) -> int:
        ri_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        i = 0
        tot = 0
        while i < len(s):
            if s[i : i + 2] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                c = s[i : i + 2]
                tot += ri_dict[c]
                i = i + 2
            else:
                c = s[i]
                tot += ri_dict[c]
                i = i + 1
        return tot

sol = Solution()

# Examples given:
s = 'III'
print (sol.romanToInt(s))

s = 'LVIII'
print (sol.romanToInt(s))

s = "MCMXCIV"
print (sol.romanToInt(s))
