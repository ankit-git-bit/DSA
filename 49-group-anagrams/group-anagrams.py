class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map=defaultdict(list)
        for words in strs:
            anagram_sort="".join(sorted(words))
            anagram_map[anagram_sort].append(words)
        return list(anagram_map.values())
