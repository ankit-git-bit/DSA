class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,j in enumerate(nums):
            diff=target-j
            if diff in dic:
                return [dic[diff],i]
            dic[nums[i]]=i
        return []

            