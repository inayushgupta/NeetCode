class Solution:
    def rob(self, nums: List[int]) -> int:

        # if I am robbing house I can either rob
        # the current house and leave the house before
        # or do not rob and take the previous value

        two_back, one_back = 0, 0

        for curr_house in nums:
            one_back, two_back = max(two_back + curr_house, one_back), one_back

        return one_back
