class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        length = 0

        while length < len(candidates) and candidates[length] <= target:
            length += 1

        if length == 0:
            return []

        res = []
        intermediate = []
        remaining = target

        def helper(start):

            nonlocal remaining

            if not remaining:
                res.append(intermediate.copy())
                return
            
            if start == length or remaining - candidates[start] < 0:
                return
            
            for index in range(start, length):

                if index > start and candidates[index] == candidates[index-1]:
                    continue

                intermediate.append(candidates[index])
                remaining -= candidates[index]

                helper(index+1)

                intermediate.pop()
                remaining += candidates[index]
        
        helper(0)
        return res