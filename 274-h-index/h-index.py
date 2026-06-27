class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        paper_citation=[0]*(n+1)

        for citation in citations:
            paper_citation[min(citation,n)] += 1

        h=n
        papers=paper_citation[n]
        while papers<h:
            h-=1
            papers+=paper_citation[h]
        return h
