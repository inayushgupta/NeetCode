class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        l = len(nums)

        def helper(subset,n):
            ans.append(subset.copy())
            #exit condition
            if n >= l: return

            for i in range(n, l):
                subset.append(nums[i])
                helper(subset, i+1)

                #backtrack
                subset.pop()
        
        helper([], 0)

        return ans
        