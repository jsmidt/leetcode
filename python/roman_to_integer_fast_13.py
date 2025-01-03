class Solution:
    def romanToInt(self, s: str) -> int:
        # Define the dictionary for single roman numeral values
        ri_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        prev_value = 0

        # Iterate through the string in reverse
        for char in reversed(s):
            curr_value = ri_dict[char]

            # If the current value is less than the previous value, it's a subtraction case
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value

            prev_value = curr_value

        return total

# Testing
sol = Solution()

# Examples given:
s = 'III'
print(sol.romanToInt(s))  # Output: 3

s = 'LVIII'
print(sol.romanToInt(s))  # Output: 58

s = "MCMXCIV"
print(sol.romanToInt(s))  # Output: 1994
