class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        intermediate = []

        def generate(start):

            if start > len(nums):
                return
            
            res.append(intermediate[:])
            for index in range(start, len(nums)):
                if start < index and nums[index] == nums[index - 1]:
                    continue
                
                intermediate.append(nums[index])
                generate(index+1)
                intermediate.pop()
            
        generate(0)
        return res