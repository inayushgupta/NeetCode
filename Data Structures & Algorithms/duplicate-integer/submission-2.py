class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for v in counter.values():
            if v != 1:
                return True
        return False