class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        max_count=0

        for n in num_set:
            if n-1 not in num_set:
               y=n+1
               while y in num_set:
                y+=1
               max_count=max(max_count,y-n)
        return max_count