class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        used = [False] * len(nums)
        
        def helper(perm):
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    perm.append(nums[i])

                    helper(perm)

                    perm.pop()
                    used[i] = False       
        helper([])

        return ans