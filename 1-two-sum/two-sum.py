class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for l in range(0,n):
            diff=target-nums[l]
            for r in range(l+1,n):
                if nums[r]==diff:
                    return [l,r]
            
            

            