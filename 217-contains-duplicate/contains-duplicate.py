class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s1=set(nums)
        return len(s1)!=len(nums)