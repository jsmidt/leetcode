# Author: Joseph Smidt
# 1769. Minimum Number of Operations to Move All Balls to Each Box

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        dist = []
        lenn = len(boxes)
        tot = [0]*lenn
        for i in range(len(boxes)):
            dist = [int(boxes[i])*abs(i - j) for j in range(lenn)]
            tot = [x + y for x, y in zip(tot, dist)]

        return tot

boxes = "001011"
sol = Solution()
print (sol.minOperations(boxes))
