class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count={}
        for i in range(len(s)):
            count[s[i]]=1+count.get(s[i],0)
        for j in t:
            if j not in count or count[j]==0:
                return False
            count[j]-=1
        return True