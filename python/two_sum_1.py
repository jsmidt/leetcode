# Author: Jospeh Smidt
#
# O(n^2) brute force solution

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lenn = len(nums)
        for i in range(0,lenn):
            for j in range(i+1,lenn):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Test on examples
sol = Solution()

# Example 1
nums = [2,7,11,15]
target = 9
print (sol.twoSum(nums, target))

# Example 2
nums = [3,2,4]
target = 6
print (sol.twoSum(nums, target))

# Example 3
nums = [3,3]
target = 6
print (sol.twoSum(nums, target))

