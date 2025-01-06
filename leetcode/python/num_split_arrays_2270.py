class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        total_sum = sum(nums)  # Calculate the total sum once
        left_sum = 0
        splits = 0

        for i in range(len(nums) - 1):
            left_sum += nums[i]  # Incrementally build the left sum
            right_sum = total_sum - left_sum  # Calculate the right sum

            if left_sum >= right_sum:
                splits += 1

        return splits


nums = [2,3,1,0]

sol = Solution()
print (sol.waysToSplitArray(nums))
