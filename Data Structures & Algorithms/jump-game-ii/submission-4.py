class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        reached = 0
        goal = n-1
        jumps = 0

        # from reached check where I can land the maximum
        while reached != goal:
            current_best_index = reached
            for index in range(reached, reached+nums[reached]+1):
                
                if index >= goal:
                    return jumps + 1

                if nums[index] + index > nums[current_best_index] + current_best_index: 
                    current_best_index = index
            
            jumps += 1
            reached  = current_best_index
        return jumps

