class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n_set = set(nums)
        if len(nums) != len(n_set):
            return True
        return False
