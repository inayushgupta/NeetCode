class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        current = 0

        for n in nums:
            match n:
                case 1:
                    current += 1
                    longest = max(longest, current)
                case 0:
                    current = 0
        return longest