class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        max_len=0
        if not s:
            return 0

        for r in range(len(s)):
            while len(s[l:r+1])!=len(set(s[l:r+1])):
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len
