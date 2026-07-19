class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        s=set(nums)
        num=list(s)
        num.sort()
        max_count=0
        count=0
        for l in range(1,len(num)):
            if num[l]==num[l-1]+1:
                count+=1
            else: count=0
            max_count=max(max_count,count)
        return max_count+1