class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        intermediate = []
        summation = 0
        length = len(nums)

        def helper(start):
            nonlocal summation

            if summation == target:
                res.append(intermediate[:])
                return
            
            if summation > target:
                return
            
            for index in range(start, length):

                summation += nums[index]
                intermediate.append(nums[index])

                helper(index)

                summation -= nums[index]
                intermediate.pop()

        helper(0)
        return res