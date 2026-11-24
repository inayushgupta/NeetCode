class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        def robit(start, end):

            one, two = 0, 0

            for i in range(start, end):
                one, two = max(one, two + nums[i]), one

            return one

        return max(robit(0, n - 1), robit(1, n))
