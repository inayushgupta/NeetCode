class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        res = []
        left = 0
        maxindex = 0

        for i in range(k):

            if nums[maxindex] < nums[i]:
                maxindex = i

        res.append(nums[maxindex])

        for right in range(k, len(nums)):
        
            left += 1

            if maxindex >= left:
                if nums[right] > nums[maxindex]:
                    maxindex = right
            else:
                maxindex = left
                for i in range(left+1, right+1):
                    if nums[maxindex] < nums[i]:
                        maxindex = i
            res.append(nums[maxindex])

        return res
